from django.shortcuts import render
import urllib3
import boto3
import urllib3
import os

# Create your views here.
def index(request):
    return render(request,'analysis/index.html')


def submit(request):
    if(request.method == 'POST'):
        fileToUpload = request.FILES.get('file')
        print(request.FILES.get('file'))
        s3 = boto3.client(
            "s3",
            aws_access_key_id=os.environ['MINIO_ACCESS'],
            aws_secret_access_key=os.environ['MINIO_SECRET'],
            endpoint_url='http://{}:{}'.format(os.environ['MINIOSERVER_SERVICE_HOST'],os.environ['MINIOSERVER_SERVICE_PORT']),
        )

        s3.put_object(Bucket="analysis",Key=fileToUpload.name, Body=fileToUpload)
        http = urllib3.PoolManager()
        website = 'http://{}:{}/analysis/{}'.format(os.environ['FLASKSERVER_SERVICE_HOST'],os.environ['FLASKSERVER_SERVICE_PORT'],fileToUpload.name)
        response = http.request('GET',website).data.decode('utf-8')
        
        return render(request, 'analysis/index.html' ,{
           'model_respose': response
        })
    return render(request, 'analysis/index.html')
