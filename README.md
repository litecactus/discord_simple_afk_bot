# A discord simple AFK bot
A really simple discord bot that toggles you AFK.

Send .afk and it will prefix your nickname with [AFK] . If you send .afk again it will remove the prefix. The code also deletes the .afk messages to keep the channel clean otherwise it gets a bit crazy. This is all it does. 

You need the discord.py module installed > https://pypi.org/project/discord.py/

**pip install discord.py**

Run on boot with crontab with

**@reboot python3 /home/user/bot.py &**

updated 22/12/2022
