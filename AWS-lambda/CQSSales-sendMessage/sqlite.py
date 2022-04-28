import sqlite3
import boto3
import os

SELECT_PRODUCT = "SELECT * FROM Products WHERE id=:id";
UPDATE_PRODUCT = "UPDATE Products SET price = ?, majorBidder = ? WHERE id = ?";

class SQLite:
    
    def __init__(self, bucket, file):
        self.con = sqlite3.connect(file)
        self.cur = self.con.cursor()
        self.bucket = bucket
        self.file = file
        pass

    def check_price(self, msg):
        id = msg['message']['id']
        price = msg['message']['price']
        
        self.cur.execute(SELECT_PRODUCT, {"id": id})
        product = self.cur.fetchone()
        
        return price > product[2]
        
        
    def update_price(self, s3, msg):
        id = msg['message']['id']
        price = msg['message']['price']
        majorBidder = msg['message']['majorBidder']
        
        self.cur.execute(UPDATE_PRODUCT,(price, majorBidder, id))
        self.con.commit()
        
        print("product "+str(id)+" updated by "+majorBidder+" with price: "+str(price)+"!")
        self.create_db_file(s3)
        
    def create_db_file(self, s3):
        f = open(self.file, "rb")
        
        s3.put_object(ACL='public-read', Bucket=self.bucket, Key=self.file.replace("/tmp/",""), 
        Body=f.read(), CacheControl="max-age=0,no-cache,no-store,must-revalidate",
            ContentType="binary/octet-stream")
        
        os.remove(self.file)
        
    def close_connection(self):
        self.cur.close()
        self.con.close()