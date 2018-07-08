from flask import Flask,request, redirect, url_for, flash,jsonify
from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
import botocore
import pandas
import boto3
import os


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/<bucketName>/<fileName>')
def compute_api(bucketName,fileName):
    s3 = boto3.client(
        "s3",
        aws_access_key_id=os.environ['MINIO_ACCESS'],
        aws_secret_access_key=os.environ['MINIO_SECRET'],
        endpoint_url='http://'+os.environ['IP_MINIO']+':9000',
    )
    
    messageObject = s3.get_object(Bucket=bucketName,Key=fileName) 
    message = messageObject["Body"].read().decode('utf-8')
    modal = joblib.load(open('SpamClassifier.pkl', 'rb'))
    Vectorizer = joblib.load(open('vectorizer.pkl', 'rb'))
    vectorize_message = Vectorizer.transform([message])
    return(modal.predict(vectorize_message)[0])
    
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')