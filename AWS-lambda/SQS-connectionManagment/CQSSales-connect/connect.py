import json
import boto3

SQS_ACCESS_KEY='ACCESS_KEY'
SQS_SECRET_KEY='SECRET_KEY'
SQS_URL='SQS_URL'

def lambda_handler(event, context):
    
    sqsClient = boto3.client("sqs",aws_access_key_id=SQS_ACCESS_KEY, aws_secret_access_key=SQS_SECRET_KEY)
    
    print(event)
    print("****")
    print(context)
    
    connectionId = event['requestContext']['connectionId']
    config = { "connectionId": connectionId }
    
    sqsClient.send_message(QueueUrl=SQS_URL, MessageBody=json.dumps(config))
    
    
    return {'statusCode': 200}
