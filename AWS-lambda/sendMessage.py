import json
import urllib3
import boto3

ACCESS_KEY='ACCESS_KEY'
SECRET_KEY='SECRET_KEY'
BUCKET_NAME='BUCKET_NAME'
TEMPALTE_FILE='connections.config'

client = boto3.client('apigatewaymanagementapi', endpoint_url="API_GATEWAY_URL")
s3 = boto3.client("s3",aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

def lambda_handler(event, context):
    # Read connections from S3
    obj = s3.get_object(Bucket=BUCKET_NAME, Key=TEMPALTE_FILE)
    
    config = obj['Body'].read().decode('utf-8')
    
    connections = config.split(";")
    del connections[-1]
    
    connectionId=event['requestContext']['connectionId']
    
    #Send messages to every connection but the origin 
    for conn in connections:
        if conn != connectionId:
            client.post_to_connection(ConnectionId=conn, Data=event['body'])
    
    
    return {'statusCode': 200}
