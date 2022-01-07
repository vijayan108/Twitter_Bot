import tweepy
import time

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

try: 
    print("Welcome To twitter Bot: \n " 
            "1. Press '1' for get the you following people: \n"
            " 2. Press '2' for get the followers : \n"
            " 3. Press '3' for like the given string post and it has count to how many tweets you need to like : \n"
            " 4. Press '4' for like retweet for given string"
            )
    value = int(input("Enter a number from the option : "))
except (TypeError,ValueError):
    print("please try again, given wrong input")

#this will verify the authorisation

api = tweepy.API(auth)
user = api.verify_credentials()
print("Your Details are : ")
print(user.name) #prints your name.
print(user.screen_name)
print(user.followers_count)

# Check the condition+
def limit_rate(cursor):
  while True:
    try:
      yield cursor.next()
    except tweepy.TweepyException:
      time.sleep(1000)
    except (StopIteration,NameError):
        break


if value == 1: # This check following people
  print("The following people are:")
  for follower in limit_rate(tweepy.Cursor(api.get_friends).items()):
         print(follower.name)
         

elif value == 2 : # This Check the followers
  print("The followers are :")
  for followers in limit_rate(tweepy.Cursor(api.get_followers).items()):
        print(followers.name)

elif value == 3: # This like the tweet of your give string
    string = input("Enter a text to search : " )
    count = int(input("Enter a number of tweet to like:"))
    for like in tweepy.Cursor(api.search_tweets,string).items(count):
          id = like.id
         # print(id)
          api.create_favorite(id)
          print(" liked that tweet") 

elif value == 4: 
    strings= input("Enter a text to search : " )
    counts = int(input("Enter a number of tweet to like:"))
    for retweet in tweepy.Cursor(api.search_tweets,strings).items(counts):
        api.retweet(retweet.id)
        print("it is retweeted")
# for follower in tweepy.Cursor(api.get_friends).items():

else:
    print("Something Wrong ,Try again")