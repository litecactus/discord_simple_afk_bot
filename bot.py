import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command(pass_context=True)
async def afk(ctx):
    x = "[AFK] "
    current_nick = ctx.author.nick
    if x in current_nick:
        old_nick = current_nick[6:]
        await ctx.author.edit(nick=old_nick)
    else:
         await ctx.author.edit(nick="[AFK] "+current_nick)
    await ctx.channel.purge(limit=1)
    
    

client.run('enter_your_token')
