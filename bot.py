from multiprocessing import context
import os
import discord
import random
import pandas
import pickle
from dotenv import load_dotenv
from discord.ext import commands
import datetime

load_dotenv()
TOKEN=os.getenv('DISCORD_TOKEN')
GUILD=os.getenv('DISCORD_GUILD')


#This is the client Object
# client=discord.Client()
client = commands.Bot(command_prefix=__import__("config").PREFIX)

#Triggers on client events
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    x={"Profile": ['TRE Bot'], "Level": [0]}

    #loads and increments at use
    with open('profiles_pickle.p', 'rb') as f:
        pickleobject=pickle.load(f)
        #Auto Lvl the first slot.  It could be prepped into a dataframe in the future.
        pickleobject['Level'][0]+=1
        pickleobject['Profile'][0]=="TRE Bot"
        print(f"Here are your contents {pickleobject}")
    
    #saves
    with open('profiles_pickle.p', 'wb') as f:
        pickle.dump(pickleobject, f)

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, welcome to the TRE Discord Server!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    trehistory= [
        "The Raven Elite was formed during the PS3 ERA on MAG.  The game had 300 active players in 150 vs 150 battles.  Each squad had 8 players and 1 Squad Leader.  4 Squads made up 1 platoon.  Each platoon had 1 Platoon Leader.  1 Company had 4 platoons.  Each Company had 1 OIC Officer in Charge."]

    squad= ["Sniper Class -- Falcon 8, Snake Eyes"]
    
    getcsv=pandas.read_csv("my_csv.csv")
    getrebirth=pandas.read_csv("rebirth_csv.csv")

    if message.content == 'trehistory':
        response = random.choice(trehistory)
        await message.channel.send(response)

    elif message.content == 'treroster':
        rosterprompt=['Which member of the TRE would you like to learn about?']
        await message.channel.send(rosterprompt[0])

    elif message.content == 'trekills':
        await message.channel.send(getcsv[['Names', 'Kills']].sort_values(by='Kills', ascending=False))

    elif message.content == 'trekpg':
        await message.channel.send(getcsv[['Names', 'Avg Kills PG']].sort_values(by='Avg Kills PG', ascending=False))

    elif message.content == 'tredpg':
        await message.channel.send(getcsv[['Names', 'Avg Deaths PG']].sort_values(by='Avg Deaths PG', ascending=False))

    elif message.content == 'trekdr':
        await message.channel.send(getcsv[["Names", "KDR"]].sort_values(by='KDR', ascending=False))
    
    elif message.content == 'trerevives':
        await message.channel.send(getcsv[["Names", "Avg Revives PG"]].sort_values(by='Avg Revives PG', ascending=False))

    elif message.content == 'trecontracts':
        await message.channel.send(getcsv[["Names", "Avg Contracts PG"]].sort_values(by='Avg Contracts PG', ascending=False))

    elif message.content == 'trescore':
        await message.channel.send(getcsv[["Names", "Avg Score"]].sort_values(by='Avg Score', ascending=False))

    elif message.content == 'tretop5%':
        await message.channel.send(getcsv[['Names', 'Top 5 Appearance %']].sort_values(by='Top 5 Appearance %', ascending=False))
    
    elif message.content == 'tretop10%':
        await message.channel.send(getcsv[['Names', 'Top 10 Appearance %']].sort_values(by='Top 10 Appearance %', ascending=False))
    
    elif message.content == 'tretop25%':
        await message.channel.send(getcsv[['Names', 'Top 25 Appearance %']].sort_values(by='Top 25 Appearance %', ascending=False))

    #new
    elif message.content == 'tretop10win%':
        await message.channel.send(getcsv[['Names', 'Top 10 Win %']].sort_values(by='Top 10 Win %', ascending=False))

    elif message.content == 'trewins':
        await message.channel.send(getcsv[['Names', 'Wins']].sort_values(by='Wins', ascending=False))

    #new
    elif message.content == 'trelikelytoengage':
        await message.channel.send(getcsv[['Names', 'Likely to Engage Rating']].sort_values(by='Likely to Engage Rating', ascending=False))
    #new
    elif message.content == 'treweratio':
        await message.channel.send(getcsv[['Names', 'Wins to Engagement Rating Ratio']].sort_values(by='Wins to Engagement Rating Ratio', ascending=False))

    elif message.content == 'rebirthwins':
        await message.channel.send(getrebirth[['Names', 'Wins']].sort_values(by='Wins', ascending=False))

    elif message.content == 'rebirthkills':
        await message.channel.send(getrebirth[['Names', 'Kills']].sort_values(by='Kills', ascending=False))
    
    elif message.content == 'rebirthkdr':
        await message.channel.send(getrebirth[['Names', 'KDR']].sort_values(by='KDR', ascending=False))

    elif message.content == 'rebirthwin%':
        await message.channel.send(getrebirth[['Names', 'Top 5 Win %']].sort_values(by='Top 5 Win %', ascending=False))

    elif message.content == 'trebotlvl':
        with open('profiles_pickle.p', 'rb') as f:
            pickleobject=pickle.load(f)
        await message.channel.send(f"TRE Bot lvl is at {pickleobject['Level'][0]}")

    # not implemented
    elif message.content == 'missions':
        await message.channel.send("Earn TRE Leaderboard EXP by completing missions.  Mission announcements coming soon...")

    # not implemented
    elif message.content == 'user':
        z=client.get_user(950992258654674975)
        await message.channel.send(f"Here is the user name {str(z)}")
    
    elif '/embed' in message.content.lower():
        embed = discord.Embed(
            title='Bounty Challenge 1: Win a Rebirth Island without any Redeploys from all squadmates and less than 8 Kills combined.',
            description='This is an open bounty.  (Screen shot post if this challenge is met)',
            color = discord.Color.random()
        )
        await message.channel.send(embed=embed)

   
       
            

        


# @client.event
# async def on_message(message):
    # if 'happy birthday' in message.content.lower():
        # await message.channel.send('Happy Birthday!')

# Use postional arguments in lists to access the list without any brackets.
client.run(TOKEN)