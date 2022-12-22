import discord
from discord.ext import commands
global x
x = "[AFK] "
intents = discord.Intents.all()
client = commands.Bot(command_prefix = '.', intents=intents)

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command(pass_context=True)
async def afk(ctx):
    global x
    global z
    current_nick = ctx.author.nick
    if x in current_nick:
        old_nick = current_nick.replace(x,"")
        await ctx.author.edit(nick=old_nick)
    else:
         await ctx.author.edit(nick=x+current_nick)
    await ctx.channel.purge(limit=1)

client.run('enter token here')
