# Saya Music
# -----------------------------------------------------------------------

# -- inside helpers.py ------------------------------------------------
HELP_1_PROMO = """
<b><u>promotion / demotion</u></b>
available commands for moderation, promotion (admins only):

- /promote <user>: grants limited admin rights. (can use reply, @username or ID)
- /fullpromote <user>: grants all possible admin permissions to the user.
- /demote <user>: removes all admin privileges from the user.
- /tempadmin <user> x(m /h /d): temporary promotion for x time. auto-demotes after x. (e.g. - /tempadmin @user 3h)

<b> all commands support:</b> reply, @username, or user ID

"""

HELP_1_PUNISH = """
<b><u>punishment / policing</u></b>
available commands for moderation, promotion (admins only):

 - /ban <user>: permanently bans the user from the group.
 - /unban <user>: revokes a ban.
 - /kick <user>: temporarily removes a user. (auto-unban after 2s)
 - /kickme: self-eject from group. (auto-unban after 3s)
 - /mute <user>: prevents a user from sending messages.
 - /tmute <user> x(m /h /d): temp mute for x time.
 - /unmute <user>: lifts a mute.
 - /tban <user> x(m /h /d): temporary ban with duration.
 - /sban <user>: silent ban without notification.
 - /dban (reply only): deletes a message and bans the sender.

 <b> all commands support:</b> reply, @username, or user ID

"""
# --------------------------------------------------------------------


# -----------------------------------------------------------------------
HELP_2 = """
<b><u>admin control :</u></b>
just add <b>c</b> at the beginning of the commands to use them for the channel.

- /pause : pause the current playing stream.
- /resume : resume the paused stream.
- /skip : skip the current playing stream and start streaming the next track in the queue.
- /end or /stop : clears the queue and ends the current playing stream.
- /player : get an interactive player panel.
- /queue : shows the queued tracks list.
"""

# -----------------------------------------------------------------------
HELP_3 = """
<b><u>auth users :</b></u>

auth users can use admin rights in the bot without admin rights in the chat.

- /auth [username/user_id] : add a user to the auth list of the bot.
- /unauth [username/user_id] : remove a user from the auth users list.
- /authusers : shows the list of auth users of the group.

"""

# -----------------------------------------------------------------------
HELP_4 = """
<u><b>chat blacklist feature :</b></u> [only for sudoers]

restrict unwanted chats from using our precious bot.

- /blacklistchat [chat id] : blacklist a chat from using the bot.
- /whitelistchat [chat id] : whitelist the blacklisted chat.
- /blacklistedchats : shows the list of blacklisted chats.

"""

# -----------------------------------------------------------------------
HELP_5 = """
<b><u>block users:</b></u> [only for sudoers]

starts ignoring the blacklisted user, so that they can't use bot commands.

- /block [username or reply to a user] : block the user from our bot.
- /unblock [username or reply to a user] : unblock the blocked user.
- /blockedusers : shows the list of blocked users.

"""

# -----------------------------------------------------------------------
HELP_6 = """
<b><u>channel play :</u></b>
you can stream audio/video in the channel.

- /cplay : starts streaming the requested audio track on the channel's video chat.
- /cvplay : starts streaming the requested video track on the channel's video chat.
- /cplayforce or /cvplayforce : stops the ongoing stream and starts streaming the requested track.
- /channelplay [chat username or id] or [disable] : connect a channel to a group and start streaming tracks by using commands sent in the group.

"""

# -----------------------------------------------------------------------
HELP_7 = """
<b><u>extra :</u></b>
Handy utilities that aren't music-related.

- /carbon  generates a carbon code image from a code snippet.
- /speedtest  measures the internet speed.
- /webdl  enter the link of a website after the command to get the source code of that website.
- /tgm  uploads a photo (under 5mb) to the cloud and provides a link.
- /tr  translates text.
- /short  enter the link that you want to shorten after the command.

"""

# -----------------------------------------------------------------------
HELP_8 = """
<b><u>global ban feature</b></u> [only for sudoers]:

- /gban [username or reply to a user] : globally bans the user from all the served chats and blacklists them from using the bot.
- /ungban [username or reply to a user] : globally unbans the globally banned user.
- /gbannedusers : shows the list of globally banned users.

"""

# -----------------------------------------------------------------------
HELP_9 = """
<u><b>broadcast feature</b></u> [only for sudoers]:

/broadcast [message or reply to a message] : broadcast a message to served chats of the bot.

<u>broadcast modes:</u>
<b>-pin</b>: pins your broadcasted messages in served chats.
<b>-pinloud</b>: pins your broadcasted message in served chats and sends a notification to the members.
<b>-user</b>: broadcasts the message to the users who have started your bot.
<b>-assistant</b>: broadcasts your message from the assistant account of the bot.
<b>-nobot</b>: forces the bot to not broadcast the message.

<b>example:</b> <code>/broadcast -user -assistant -pin Testing broadcast</code>
"""

# -----------------------------------------------------------------------
HELP_10 = """
<b><u>games :</u></b>
Telegram emoji games - quick fun.

- /dice   - /dart   - /basket   
- /ball   - /football   - /jackpot 
"""

# -----------------------------------------------------------------------
HELP_11 = """
<b><u>chatgpt :</u></b>

<b><u>Chat-with-AI features.</u></b>

<i>coming soon...</i>
"""

# -----------------------------------------------------------------------
HELP_12 = """
<b><u>info :</u></b>
Look up user, group or random IDs.

- /id : get the current group id. if used by replying to a message, gets that user's id.
- /info : get information about a user.
- /github <username> : get information about a github user.
- /sg : reply to an id or username to get the history of that person.
- /groupdata & /groupinfo : to get group info.
- /whois : reply or tag a username to know details of that person.
"""

# -----------------------------------------------------------------------
HELP_13 = """
<b><u>image :</u></b>
AI drawing & editing.

- /getdraw  generates a drawing based on a given prompt.
- /upscale  reply to an image to upscale it and improve its quality.
- /rmbg  removes the background from an image.

"""

# -----------------------------------------------------------------------
HELP_14 = """
<u><b>log / maintenance :</b></u>  (sudo)
Keep the bot healthy.

- /logs - Get latest Railway/Docker logs.
- /logger enable - Start live message logging.  
- /maintenance enable - Bot replies "Under maintenance".  
- /update - Git pull & PM you the diff.  
- /restart - Graceful reboot.
"""

# -----------------------------------------------------------------------
HELP_15 = """
<b><u>loop :</u></b>
starts streaming the ongoing stream in a loop.

- /loop [enable/disable] : enables or disables loop for the ongoing stream.
- /loop [1, 2, 3, ...] : sets the loop to the specified number of times.

"""

# -----------------------------------------------------------------------
HELP_16 = """
<b><u>group management :</u></b>

- /pin : pins a message in the group.
- /unpin : unpins the currently pinned message.
- /staff : displays the list of staff members.
- /bots : displays the list of bots in the group.
- /settitle : sets the title of the group.
- /setdescription : sets the description of the group.
- /wel : turn welcome messages on or off.
- /setphoto : sets the group photo.
- /removephoto : removes the group photo.
- /zombies : removes deleted accounts from the group.
- /imposter on/off : turns on or off the watcher for your group, which notifies about users who change their name or username.
- /lang : change the bot language.

"""

# -----------------------------------------------------------------------
HELP_17 = """
<b><u>masti   (fun):</u></b>
Random social mini-games.

- /couple - Pick today's random pair.  
- /love Alice Bob - % compatibility.  
- /cute, /hot, /gay, /sexy, /horny ... - Self-rating fun.  
- /kiss, /hug, /slap - Role-play replies.  
- /sleep - Bot tells you good night.  
- /wish Happy birthday! - Sweet wish card generator.  
"""

# -----------------------------------------------------------------------
HELP_18 = """
<b><u>mass actions :</u></b>
Heavy maintenance tools - <b>use with caution.</b>

- /deleteall  deletes all messages in the group.
- /kickall  kicks all members in the group.
- /banall  bans all members in the group.
- /unbanall  unbans all members in the group.
- /muteall  mutes all members in the group.
- /unmuteall  unmutes all members in the group.
- /unpinall  unpins all pinned messages in the group. 
- /purge or /spurge - Smaller scale deletions.
"""

# -----------------------------------------------------------------------
HELP_19 = """
<b><u>ping & stats :</u></b>

- /start : starts the music bot.
- /help : get help menu with explanation of commands.
- /ping : shows the ping and system stats of the bot.
- /stats : shows the overall stats of the bot.

"""

# -----------------------------------------------------------------------
HELP_20 = """
<b><u>play :</u></b>
<b>v :</b>stands for video play.
<b>force :</b>stands for force play.

- /play or /vplay : starts streaming the requested track on video chat.
- /playforce or /vplayforce : stops the ongoing stream and starts streaming the requested track.

"""

# -----------------------------------------------------------------------
HELP_21 = """
<b><u>repo info :</u></b>

- /allrepo  enter the github username after the command to get all repositories of that account.
- /pypi  enter the project name after the command to get stats of that project [project = github repositories].
- /downloadrepo  enter the repository link after the command to download the repository.

"""

# -----------------------------------------------------------------------
HELP_22 = """
<b><u>search :</u></b>

- /anime <query> : search myanimelist for the given query.
- /mongochk : check the status of your mongodb instance [enter the mongodb link after the command].
- /ip : enter the ip address after the command to get info about that ip.
- /domain : enter the domain name after the command to find info about the domain.
- /weather : enter the location after the command to get the weather of that location.

"""

# -----------------------------------------------------------------------
HELP_23 = """
<b><u>seek :</u></b>
Jump inside the currently playing media.

- /seek [duration in seconds] : seek the stream to the given duration.
- /seekback [duration in seconds] : backward seek the stream by the given duration.

"""

# -----------------------------------------------------------------------
HELP_24 = """
<b><u>shuffle :</u></b>
Randomise the queue.

- /shuffle : shuffles the queue.
- /queue : shows the shuffled queue.
"""

# -----------------------------------------------------------------------
HELP_25 = """
<b><u>song / download :</u></b>

- /movie : to get information about a movie.
- /extract [video or audio] : reply to a video file to remove audio or video from it.

"""

# -----------------------------------------------------------------------
HELP_26 = """
<b><u>speed :</u></b>
Alter playback speed.

- /speed 1.25 - 25 % faster.  
- /playback 0.5 - Half speed.  
- /cspeed / /cplayback - Same but for linked channel.
"""

# -----------------------------------------------------------------------
HELP_27 = """
<b><u>sticker :</u></b>

- /mmf  to memify the image or sticker.
- /tiny  reply to a sticker that you want to make tiny.
- /kang  this command is used to kang images into stickers.
- /packkang  creates a pack of stickers from another pack.
- /stid  gets the sticker id of a sticker.
- /meme  use this command to generate memes.
- /stdl  to download the sticker.
"""

# -----------------------------------------------------------------------
HELP_28 = """
<b><u>tag-all :</u></b>
Mention everyone - responsibly!

- /utag or /mention or /all  enter the text after the command or reply to a text to mention all.
- /cancel or /ustop  to cancel mentioning.
- /tagall  for randomly funny tags .
- /tagoff or /tagstop  stop mentioning funny tags.
- /gmtag  for morning wishes .
- /gmstop  stop morning wishes.
- /gntag  for night wishes .
- /gnstop  stop night wishes .
- /hitag  tag members with hindi quotes.
- /histop  stop hindi quotes.
- /lifetag  tag members with english quotes.
- /lifestop  stop english quotes.
- /shayari  tag all members with shayari .
- /shayarioff  stop mentioning shayari.
"""

# -----------------------------------------------------------------------
HELP_29 = """
<b><u>text editing :</u></b>

these are the commands for text editing or designing:

- /font or /fonts  enter the text after the command to generate font effects.
- /code  enter the text after the command to format it as code.
- /genpw  to generate a strong password.
- /write  enter the text after the command to write in a notebook style.
- /qr  enter the text after the command to generate a qr code of the text.

<b><u>Quote Module:</b></u>
- /q  reply to a message to create a quote from it.
- /q r  reply to a message to create a quote from the message and its replied message.
- /q <count>  reply to a message with a number to quote that message and the next messages up to 10.
- /q <count> r  reply to a message with a number and 'r' to quote that message, its replied message, and the next messages up to 10.

"""
# -----------------------------------------------------------------------
