import json
import urllib3
import boto3


SQS_ACCESS_KEY='ACCESS_KEY'
SQS_SECRET_KEY='SECRET_KEY'
SQS_URL='SQS_URL'

sqsClient = boto3.client("sqs",aws_access_key_id=SQS_ACCESS_KEY, aws_secret_access_key=SQS_SECRET_KEY)

def lambda_handler(event, context):
    
    connectionId=event['requestContext']['connectionId']
    
    del_connection(connectionId)
    
    return {'statusCode': 200}

def del_connection(connectionId):
    connList=[]
    
    numMsg = int(count_messages_queue())
    
    while numMsg == 0:
        numMsg = int(count_messages_queue())
        
    connections = sqsClient.receive_message(QueueUrl=SQS_URL, MaxNumberOfMessages=1, WaitTimeSeconds=5)
    
    while numMsg > 0:
        for conn in connections['Messages']:
            connAux = json.loads(conn['Body'])['connectionId']
            print(connAux)
            if connAux == connectionId:
                sqsClient.delete_message(QueueUrl=SQS_URL,ReceiptHandle=conn['ReceiptHandle'])
                numMsg = 0
            else:
                connList.append(connAux)
                connections = sqsClient.receive_message(QueueUrl=SQS_URL, MaxNumberOfMessages=1, WaitTimeSeconds=5)
                numMsg -= 1
    print(connList)
    for conn in connList:
        config = { "connectionId": conn }
        sqsClient.send_message(QueueUrl=SQS_URL, MessageBody=json.dumps(config))
        
    return connList
    
def count_messages_queue():
    attributes = sqsClient.get_queue_attributes(QueueUrl=SQS_URL, AttributeNames=['ApproximateNumberOfMessages'])
    return attributes['Attributes']['ApproximateNumberOfMessages']