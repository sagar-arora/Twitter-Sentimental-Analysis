import mysql.connector
import time

conn=mysql.connector.connect(user="root",host="localhost",password="sagar",database="python")
c=conn.cursor()
username='python'

tweet='man im so cool'

c.execute("INSERT INTO tweets (time_now, username, tweet) VALUES (%s,%s,%s)",
            (time.time(), username, tweet))

conn.commit()            
