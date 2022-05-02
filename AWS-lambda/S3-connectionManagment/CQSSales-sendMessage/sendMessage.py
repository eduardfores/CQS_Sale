import json
import urllib3
import boto3
from sqlite import SQLite

ACCESS_KEY='ACCESS_KEY'
SECRET_KEY='SECRET_KEY'
BUCKET_NAME='BUCKET_NAME'
TEMPALTE_FILE='connections.config'

DB_FILE='database-products.db'
DB_TMP_FILE='/tmp/' + DB_FILE

WEBSOCKET='WEB_SOCKET'

client = boto3.client('apigatewaymanagementapi', endpoint_url=WEBSOCKET)
s3 = boto3.client("s3",aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

#download db file from S3 to /tmp directory
boto3.resource('s3').Bucket(BUCKET_NAME).download_file(DB_FILE, DB_TMP_FILE)
sql = SQLite(BUCKET_NAME, DB_TMP_FILE)

def lambda_handler(event, context):
    
    # Read connections from S3
    obj = s3.get_object(Bucket=BUCKET_NAME, Key=TEMPALTE_FILE)
    
    config = obj['Body'].read().decode('utf-8')
    
    connections = config.split(";")
    del connections[-1]
    
    #Get necessary data from the requests
    connectionId=event['requestContext']['connectionId']
    msg = event['body']
    
    sql.execute_SQL(s3, json.loads(msg))

    #Send messages to every connection but the origin
    for conn in connections:
        if conn != connectionId:
            client.post_to_connection(ConnectionId=conn, Data=msg)
    
    return {'statusCode': 200}

