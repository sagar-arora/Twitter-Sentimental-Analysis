import tweepy as tw
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import mysql.connector
import time
import json
ckey='AsuHypDfZQlMo3nfF5srp3t78'
csecret='G4Ua8hdRH1O7uSQvYMK2HpWHeHOmHmHzoS5BvlqL3oAJ5AIDDW'
atoken='761875896-kq51OneWKzGW2rit4nn5pIwsjWmweu0EfCqztLs5'
asecret='sIE4RVlqFyNcUiOrecd8pz0p4hdrh1cqOb3P50O87O2OL'

conn=mysql.connector.connect(user="root",host="localhost",password="sagar",database="python")
c=conn.cursor()


class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        
        tweet = all_data["text"]
        
        username = all_data["user"]["screen_name"]
        
        c.execute("INSERT INTO tweets (time_now, username, tweet) VALUES (%s,%s,%s)",
            (time.time(), username, tweet))

        conn.commit()

        print((username,tweet))
        
        return True

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["python"])

