import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

Client=discord.Client()
client=commands.Bot(command_prefix="")

@client.event
@asyncio.coroutine
def on_ready():
    print("Hello World!")

@client.event
@asyncio.coroutine
def on_message(message):
    if message.channel.id=="493819751529840652":
        l=message.content
        for i in range(len(l)):
            if l[i:i+4]=="http":
                if l.count("/")!=0:
                    yield from client.send_message(message.author,"Hey there! Please don't send links in the general channel. Your message was auto deleted by the bot made by the Sensha-do Federation.\nHere's your message if you wish to edit it:\n%s" % message.content)
                    yield from client.delete_message(message)
                    break
    if message.channel.id=="496541228771573770":
        if message.content.startswith("makematch"):
            yield from client.send_message(message.channel,"Say hello!")
                      
client.run("NTIyMTU0MDM3MjU3MTc1MDQx.DvG2cA.RTXnK_U2Yzh48ImJU9lzYxcc3lc")
