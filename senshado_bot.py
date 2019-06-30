import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import os

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
        if message.content.startswith("-botstatus"):
            yield from client.send_message(message.channel,"I'm working well here!")
            
    if message.channel.id=="538748795547025408":
        if message.content.startswith("makematch"):
            #yield from client.send_message(message.channel,"Say hello!")
            maps=[['Fulda Gap'], ['Second Battle of El Alamein'], ['Frozen Pass'],
               ['Berlin'], ['Eastern Europe (small)', 'European Province (large)'],
               ['Finland'], ['White Rock Fortress'], ['Jungle'],
               ['Battle of Hürtgen Forest'],
               ['Ash River'], ['Karelia'], ['Carpathians'], ['Kuban'], ['Kursk'],
               ['Mozdok'], ['Beach of Normandy', 'Fields of Normandy'],
               ['Poland (small)', 'Fields of Poland'], ['Port Novorossiysk'],
               ['Advance to the Rhine'], ['Stalingrad'], ['Tunisia'],
               ['Sands of Tunisia'], ['Volokolamsk (small)', 'Surroundings of Volokolamsk'],
               ['Sinai'], ['Sands of Sinai'], ['38th Parallel'], ['Abandoned Factory'],
               ['Ardennes'], ['Middle East'], ['Maginot Line'], ['Italy'],
               ['American Desert'], ['Alaska'], ['Vietnam Hills']]

            times=['Dawn', 'Morning', 'Morning', 'Morning', 'Morning', 'Noon', 'Noon', 'Noon', 'Noon', 'Noon', 'Day', 'Day', 'Day', 'Day', 'Day', 'Evening', 'Evening', 'Evening', 'Evening', 'Dusk']
            weathers=['Clear', 'Clear', 'Good', 'Good', 'Hazy', 'Thin clouds', 'Thin clouds', 'Cloudy', 'Cloudy',
                     'Overcast', 'Blind', 'Rain']

            random.shuffle(maps)
            k=message.content
            if len(k.split()) != 2:
                yield from client.send_message(message.channel,"Please respect the bot. The proper command is:\nmakematch {n}\nFor example:\nmakematch 5")
            else:
                try:
                    n = int(k.split()[1])
                    if n>10:
                        n=10

                    for i in range(n):
                        mapp=random.choice(maps[i])
                        roundd=str(i+1)
                        time=random.choice(times)
                        weather=random.choice(weathers)
                        yield from client.send_message(message.channel,"""->The map for round %s will be __**%s**__.
    The weather setting will be __**%s**__.
    The time setting will be __**%s**__.
    """ % (roundd,mapp,weather,time))
                except:
                    yield from client.send_message(message.channel,"Please respect the bot. The proper command is:\nmakematch {n}\nFor example:\nmakematch 5")


access_token= os.environ["ACCESS_TOKEN"]
client.run(access_token)
