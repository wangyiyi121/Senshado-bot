import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.utils import get
import asyncio
import random
import os
import time as UTC_Clock

Client=discord.Client()
client=commands.Bot(command_prefix="")

schoolList=['493834150613221386', '493831572160774203', '493830666497163264', '493831665295294479', '493981457539268618',
            '493829480176156682', '493830747560345600', '493826201211633684', '497048841569304586', '493962214424838165',
            '493831211937169418', '495301493830975508', '497087272001470465', '493828564949663745', '493828483982819329',
            '493830748105736202', '493981768437858305', '494603071331237930', '493829428300873728', '493830293761818634',
            '493830210689433600', '495291519117426708', '493971616569753610', '493962547255443486', '493961626198867968',
            '493971793678434305', '495293213398269972', '493971901710860314']
iconList=['<:Selection:495457986077130752> ', '<:Anzio:493969564372303874>', '<:BCFreedom:494331126731505664> ',
          '<:Bellwall:495722087638499358> ', '<:BD:524694874641924106> ', '<:Bonple:493970410581524482> ',
          '<:ChiHaTan:493971191565123584> ', '<:Count:493971570159648783> ', '<:Gilbert:557986032373465118> ',
          '<:Gregor:493970310379470848> ', '<:Jatkosota:493969722446970890>', '<:kebab:585624583026245633> ',
          '<:Koala:493971078104743947> ', '<:Kuromorimine:493969388161204244> ', '<:Ooarai:495000944417701888> ',
          '<:Maginot:493970721500954646> ', '<:Maple:493982121308848128> ', '<:Neutrality:595807586817802252> ',
          '<:Pravda:493969529072779264> ', '<:saunders:493970907606286337> ', '<:StGloriana:493971000250073099> ',
          '<:Tategoto:549055046155894804> ', '<:tatenashi:493970798231683083> ', '<:Viggen:493970207853903884> ',
          '<:Viking:498638499973562381> ', '<:Waffle:510282243504340992> ', '<:WKnotGAy:574069286595723283> ',
          '<:Yogurt:493970648473796613>']
SWList=['595024594600198164', '595024689324228618', '595024774019940382', '595024833574600705', '595024912423321600', 
        '595025046838181899', '595025101531906059', '595025152019005440', '595025215893929984', '595025292465143838', 
        '595025355191091250', '595025413781192708', '595025467665285131', '595025536879951913', '595025595172257902', 
        '595025677414039553', '595025781852209162', '595025852031434752', '595030500721295362', '595030629079449601', 
        '595030690748432385']
SWIconList=['<:karlsland:613916475824013342>', '<:britannia:613916475253719054>', '<:dacia:613916474683162625>', 
            '<:farawayland:613916475874344990>', '<:fuso:613916475622948864>', '<:gallia:613916474368851984>', 
            '<:grecia:613916474171719691>', '<:hispania:613916474381172746>', '<:liberion:613916475064844329>', 
            '<:moesia:613916475903967253>', '<:aoteaora:613916473659752473>', '<:orussia:613916473295110184>', 
            '<:ostmark:613916473991102464>', '<:romagna:613916473064423444>', '<:siamro:613916478269423639>', 
            '<:southafricarepublic:613916476503490560>', '<:suomus:613916472204591106>', '<:venezia:613916475178090507>', 
            '<:australis:613916474259669026>', '<:baltland:613916476952543272>', '<:belgica:613916476243443714>']

@client.event
@asyncio.coroutine
def on_ready():
    print("Hello World!")

@client.event
@asyncio.coroutine
def on_member_update(before, after):
    if before.roles!=after.roles:
        fullList=[]
        text="Senshado School Member Count:```"
        for i in range(len(schoolList)):
            role = get(before.server.roles, id=schoolList[i])
            icon = iconList[i]
            sum = 0
            for member in before.server.members:
                if role in member.roles:
                    sum += 1
            text += role.name
            for j in range(len(role.name),34):
                text += " "
            if sum < 10:
                text += " "
            text += str(sum) + " members\n\n"
            if sum >= 35:
                fullList.append([role.name,icon])
        text += "```\n"
        for i in fullList:
            text += i[0] + " is full " + i[1] + "\n"
        #text += "\nThe member count is updated automatically.\nLast update was at " + UTC_Clock.asctime(UTC_Clock.gmtime()) + " (UTC timezone)"
        #yield from client.send_message(message.channel,text)
        
        
        msg = yield from client.get_message(client.get_channel("535235959948574740"), "594793351329349643")
        yield from client.edit_message(msg, text)
            
        #########################################

        fullList=[]
        text="Strike Witches Nation Member Count:```"
        for i in range(len(SWList)):
            role = get(before.server.roles, id=SWList[i])
            icon = SWIconList[i]
            sum = 0
            for member in before.server.members:
                if role in member.roles:
                    sum += 1
            text += role.name
            for j in range(len(role.name),34):
                text += " "
            if sum < 10:
                text += " "
            text += str(sum) + " members\n\n"
            if sum >= 35:
                fullList.append([role.name,icon])
        text += "```\n"
        for i in fullList:
            text += i[0] + " is full " + i[1] + "\n"
        text += "\nThe member count is updated automatically.\nLast update was at " + UTC_Clock.asctime(UTC_Clock.gmtime()) + " (UTC timezone)"
        #yield from client.send_message(message.channel,text)
        
        
        msg = yield from client.get_message(client.get_channel("535235959948574740"), "604856268406128640")
        yield from client.edit_message(msg, text)



@client.event
@asyncio.coroutine
def on_message(message):
    if message.channel.id=="493819751529840652":
        l=message.content.lower()
        for i in range(len(l)):
            if l[i:i+4]=="http":
                if l.count("/")!=0:
                    if not((".jpg" in l) or (".jpeg" in l) or (".png" in l) or (".gif" in l)):
                        yield from client.send_message(message.author,"Hey there! Please don't send links in the general channel. Your message was auto deleted by the bot made by the Sensha-do Federation.\nHere's your message if you wish to edit it:\n%s" % message.content)
                        yield from client.delete_message(message)
                        break
                    
    if message.channel.id=="496541228771573770":
        if message.content.startswith("-botstatus"):
            yield from client.send_message(message.channel,"I'm working well here!")
        if message.content.startswith("-iconcheck"):
            for i in range(len(schoolList)):
                role = get(message.server.roles, id=schoolList[i])
                icon = iconList[i]
                yield from client.send_message(message.channel, role.name + " " + icon)
        if message.content.startswith("-swiconcheck"):
            for i in range(len(SWList)):
                role = get(message.server.roles, id=SWList[i])
                icon = SWIconList[i]
                yield from client.send_message(message.channel, role.name + " " + icon)
        if message.content.startswith("-currenttime"):
            yield from client.send_message(message.channel,UTC_Clock.asctime(UTC_Clock.gmtime()))
    if message.channel.id=="535235959948574740":
        if message.content.startswith("thisIsAnUpdate"):
            fullList=[]
            text="Senshado School Member Count:```"
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
                text += str(sum) + " members\n\n"
                if sum >= 35:
                    fullList.append([role.name,icon])
            text += "```\n"
            for i in fullList:
                text += i[0] + " is full " + i[1] + "\n"
            #text += "\nThe member count is updated automatically.\nLast update was at " + UTC_Clock.asctime(UTC_Clock.gmtime()) + " (UTC timezone)"
            #yield from client.send_message(message.channel,text)
            
            
            msg = yield from client.get_message(message.channel, "594793351329349643")
            yield from client.edit_message(msg, text)
            #yield from client.delete_message(message)
            
            ##################################################
            
            fullList=[]
            text="Strike Witches Nation Member Count:```"
            for i in range(len(SWList)):
                role = get(message.server.roles, id=SWList[i])
                icon = SWIconList[i]
                sum = 0
                for member in message.server.members:
                    if role in member.roles:
                        sum += 1
                text += role.name
                for j in range(len(role.name),34):
                    text += " "
                if sum < 10:
                    text += " "
                text += str(sum) + " members\n\n"
                if sum >= 35:
                    fullList.append([role.name,icon])
            text += "```\n"
            for i in fullList:
                text += i[0] + " is full " + i[1] + "\n"
            text += "\nThe member count is updated automatically.\nLast update was at " + UTC_Clock.asctime(UTC_Clock.gmtime()) + " (UTC timezone)"
            #yield from client.send_message(message.channel,text)
            
            
            msg = yield from client.get_message(message.channel, "604856268406128640")
            yield from client.edit_message(msg, text)
            yield from client.delete_message(message)
            
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
