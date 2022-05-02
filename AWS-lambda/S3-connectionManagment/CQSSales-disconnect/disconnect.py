import json
import urllib3
import boto3

ACCESS_KEY='ACCESS_KEY'
SECRET_KEY='SECRET_KEY'
BUCKET_NAME='BUCKET_NAME'
TEMPALTE_FILE='connections.config'

s3 = boto3.client("s3",aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

def lambda_handler(event, context):
    
    obj = s3.get_object(Bucket=BUCKET_NAME, Key=TEMPALTE_FILE)
    
    config = obj['Body'].read().decode('utf-8')
    
    connections = config.split(";")
    del connections[-1]
    
    connectionId=event['requestContext']['connectionId']
    
    connections.remove(connectionId)
    print(connectionId+" deleted")
    
    configModified=""
    
    for conn in connections:
        configModified += conn+";"
            
    print(configModified)
    
    s3.put_object(Bucket=BUCKET_NAME, Key=TEMPALTE_FILE, Body=configModified)
    
    return {'statusCode': 200}
