import tweepy
from config import settings

botAccount = input("Please enter which source you'd like to use. \n Killas Closet \n Reshalas Bathroom \n Labs \n ->")
imageCheck = input("Do you want to upload an image? Type 1 for Yes and 2 for No \n")
###############################################
auth = tweepy.OAuthHandler((settings[botAccount]["clientKey"]), (settings[botAccount]["clientKeySecret"]))
auth.set_access_token((settings[botAccount]["accessToken"]), settings[botAccount]["accessTokenSecret"])
api = tweepy.API(auth)
###############################################

if imageCheck == "1":
    print('--------------------------------------')
    imageURL = input("Please gib ur image name \n")
    print('--------------------------------------')
    tweetText = input("Please gib tweeeet text \n") 
    media = api.media_upload(imageURL)
    api.update_status(status=tweetText, media_ids=[media.media_id])
    print('Check your Twitter, dude.')
else:
    print('--------------------------------------')
    tweetText = input("Please gib tweeeet text \n") 
    api.update_status(status=(tweetText))
    print('Check your Twitter, dude.')
