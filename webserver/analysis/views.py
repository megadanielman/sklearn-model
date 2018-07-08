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
            endpoint_url='http://'+os.environ['IP_MINIO']+':9000',
        )

        s3.put_object(Bucket="analysis",Key=fileToUpload.name, Body=fileToUpload)
        http = urllib3.PoolManager()

        response = http.request('GET', 'http://'+os.environ['IP_FLASK']+':5000/analysis/'+fileToUpload.name).data.decode('utf-8')
        
        return render(request, 'analysis/index.html' ,{
           'model_respose': response
        })
    return render(request, 'analysis/index.html')
