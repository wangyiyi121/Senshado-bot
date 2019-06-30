import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.utils import get
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
        if message.content.startswith("thisIsAnUpdate"):
            schoolList=["493831665295294479","493829428300873728","493981768437858305","493830210689433600","495301493830975508","493830293761818634"]
            iconList=["<:Bellwall:495722087638499358>","<:Pravda:493969529072779264>","<:Maple:493982121308848128>","<:StGloriana:493971000250073099>","<:kebab:585624583026245633>","<:saunders:493970907606286337>"]
            fullList=[]
            text="```"
            for i in range(len(schoolList)):
                role = get(message.server.roles, id=schoolList[i])
                icon = iconList[i]
                sum = 0
                for member in message.server.members:
                    if role in member.roles:
                        sum += 1
                text += role.name
                for j in range(len(role.name),34):
                    text += " "
                if sum < 10:
                    text += " "
                text += str(sum) + " members\n"
                if sum >= 35:
                    fullList.append([role.name,icon])
            text += "```\n"
            for i in fullList:
                text += i[0] + " is full " + i[1]
            yield from client.send_message(message.channel,text)
            
            
            #msg = yield from client.get_message(message.channel, "594769088321028116")
            #yield from client.edit_message(msg, 'updated!')
            
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
