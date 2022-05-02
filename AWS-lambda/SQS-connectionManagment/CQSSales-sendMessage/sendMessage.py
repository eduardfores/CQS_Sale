import json
import urllib3
import boto3
from sqlite import SQLite

ACCESS_KEY='ACCESS_KEY'
SECRET_KEY='SECRET_KEY'
BUCKET_NAME='BUCKET_NAME'

SQS_ACCESS_KEY='ACCESS_KEY'
SQS_SECRET_KEY='SECRET_KEY'
SQS_URL='SQS_URL'

DB_FILE='database-products.db'
DB_TMP_FILE='/tmp/' + DB_FILE
WEBSOCKET='WEB_SOCKET'

sqsClient = boto3.client("sqs",aws_access_key_id=SQS_ACCESS_KEY, aws_secret_access_key=SQS_SECRET_KEY)
    
client = boto3.client('apigatewaymanagementapi', endpoint_url=WEBSOCKET)
s3 = boto3.client("s3",aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

#download db file from S3 to /tmp directory
boto3.resource('s3').Bucket(BUCKET_NAME).download_file(DB_FILE, DB_TMP_FILE)
sql = SQLite(BUCKET_NAME, DB_TMP_FILE)

def lambda_handler(event, context):
    
    # Read connections from S3
    connections = get_messages()
    
    print(connections)
    
    #Get necessary data from the requests
    connectionId=event['requestContext']['connectionId']
    msg = event['body']
    
    sql.execute_SQL(s3, json.loads(msg))

    #Send messages to every connection but the origin
    for conn in connections:
        if conn != connectionId:
            client.post_to_connection(ConnectionId=conn, Data=msg)
    
    return {'statusCode': 200}
    
def get_messages():
    connList=[]
    
    numMsg = int(count_messages_queue())
    
    while numMsg == 0:
        numMsg = int(count_messages_queue())
        
    connections = sqsClient.receive_message(QueueUrl=SQS_URL, MaxNumberOfMessages=1, WaitTimeSeconds=5)
    
    while numMsg > 0:
        for conn in connections['Messages']:
            connList.append(json.loads(conn['Body'])['connectionId'])
            sqsClient.delete_message(QueueUrl=SQS_URL,ReceiptHandle=conn['ReceiptHandle'])
        
        numMsg -= 1
        connections = sqsClient.receive_message(QueueUrl=SQS_URL, MaxNumberOfMessages=1, WaitTimeSeconds=5)
    
    for conn in connList:
        config = { "connectionId": conn }
        sqsClient.send_message(QueueUrl=SQS_URL, MessageBody=json.dumps(config))
        
    return connList
    
def count_messages_queue():
    attributes = sqsClient.get_queue_attributes(QueueUrl=SQS_URL, AttributeNames=['ApproximateNumberOfMessages'])
    return attributes['Attributes']['ApproximateNumberOfMessages']