import sqlite3
import boto3
import os

class SQLite:
    
    def __init__(self, bucket, file):
        self.bucket = bucket
        self.file = file
        pass
        
    def execute_SQL(self, s3, msg):
        self.con = sqlite3.connect(self.file)
        self.cur = self.con.cursor()
        
        sql = msg['message']['sql']
        tup = msg['message']['data']
        
        try:
            self.cur.execute(sql, tuple(tup))
            self.con.commit()
        finally:
            self.cur.close()
            self.con.close()
            self.create_db_file(s3)
        
    def create_db_file(self, s3):
        f = open(self.file, "rb")
        
        s3.put_object(ACL='public-read', Bucket=self.bucket, Key=self.file.replace("/tmp/",""), 
        Body=f.read(), CacheControl="max-age=0,no-cache,no-store,must-revalidate",
            ContentType="binary/octet-stream")