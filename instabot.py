from instabot import Bot
bot = Bot()
#Things to do with your instagram bot
#No.1 login 
bot.login(username="your_username", password="your_password") #enter your personal username anf password
#No.2 following other users
bot.follow('username')  #enter the username you want to follow
#No.3 Uploading photo with caption
bot.upload_photo("C:/user/Desktop/photo.jpg",caption = "some caption that you have to post") #paste your path where you have the photos to be uploaded
#No.4 Unfollowing other users
bot.unfollow('username') #unfollow the username
#No.5 sending messages to multiple users
bot.send_message(["username","username2"], "Hello from your bot!") #enter the username and message you want to send
#No.6 generating the username of your own account
followers = bot.get_user_followers("your_username")
for follower in followers:
    print(bot.get_user_info(follower))
#No.7 generating the user you have been following
following = bot.get_user_following("your_username")
for Following in following:
    print(bot.get_user_info(Following))