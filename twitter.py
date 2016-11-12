import tweepy
from tweet import Tweet

def auth_setup():
    consumer_key = 'HoOTtmR9Fb38te3fSfoVp8WAx'
    consumer_secret = 'A0XCKYvBnU9JoXqxQJSsh90kfYqamUA9YB3yUyJFQfbs7sLESu'

    access_token = '64691466-uatce40p59OjYvs69eZOizftD9terGiCmgvlbNxjf'
    access_token_secret = 'ACx8cAOf3mNhtj5rdZOivzGCj4OdarbY0i5X21KM4BjEc'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    return tweepy.API(auth)

def search_tweets(tweepy, api, keyword, location, count):
    tweets = []
    i = 0
    for tweet in tweepy.Cursor(api.search, geocode = location).items(count):
    #for tweet in tweepy.Cursor(api.search, q = 'night', geocode = '37.781157,-122.398720,10mi').items(100):

            if not(tweet.coordinates is None):
                '''
                print "Author: ", tweet.author.name.encode('utf-8')
                print "Text: ", tweet.text.encode('utf-8')
                print "Location:", tweet.user.location.encode('utf8')
                print "Geolocation: ", str(tweet.geo).split("[")[1].split("]")[0]
                print "Creation: ", tweet.created_at
                print ""
                '''
                i += 1

                t = Tweet(str(tweet.author.name.encode('utf-8')), str(tweet.text.encode('utf-8')), str(tweet.user.location.encode('utf-8')), str(tweet.created_at))
                tweets.append(t)

    #print "Size of list: ", len(tweets)
    print "Count: ", i

    return tweets


api = auth_setup()
for a in search_tweets(tweepy, api, "", "37.781157,-122.398720,5mi", 1000):
    print a.to_string()
