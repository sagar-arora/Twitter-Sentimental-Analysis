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
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

user = api.get_user('twitter')
print (user.screen_name)
print (user.followers_count)
for friend in user.friends():
   print (friend.screen_name)
