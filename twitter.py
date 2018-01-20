import tweepy as tw
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
 
ckey='AsuHypDfZQlMo3nfF5srp3t78'
csecret='G4Ua8hdRH1O7uSQvYMK2HpWHeHOmHmHzoS5BvlqL3oAJ5AIDDW'
atoken='761875896-kq51OneWKzGW2rit4nn5pIwsjWmweu0EfCqztLs5'
asecret='sIE4RVlqFyNcUiOrecd8pz0p4hdrh1cqOb3P50O87O2OL'
 
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
 
api = tw.API(auth)

 
class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('python1.csv', 'a') as f:
                f.write(data)
                f.write('\n')
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#car'])
