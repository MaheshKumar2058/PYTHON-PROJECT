from instabot import Bot
bot=Bot()
bot.login(username=" ", password= " ")
bot.follow(" ")
bot.upload_photo(" ")
bot.unfollow(" ")
bot.send_message(" ")
followers=bot.get_user_followers(" ")
for follower in followers:
    print(bot.get_user_info(follower))
following=bot.get_user_following(" ")
for Following in following:
    print(bot.get_user_info(Following))