import json
import boto3

ACCESS_KEY='ACCESS_KEY'
SECRET_KEY='SECRET_KEY'
BUCKET_NAME='BUCKET_NAME'
TEMPALTE_FILE='connections.config'

s3 = boto3.client("s3",aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    
def lambda_handler(event, context):
    
    print(event)
    print("****")
    print(context)
    
    
    obj = s3.get_object(Bucket=BUCKET_NAME, Key=TEMPALTE_FILE)
    
    config = obj['Body'].read().decode('utf-8')
    
    connectionId = event['requestContext']['connectionId']
    config += connectionId+";"
    
    print(config)
    
    s3.put_object(Bucket=BUCKET_NAME, Key=TEMPALTE_FILE, Body=config)
    
    
    return {'statusCode': 200}
