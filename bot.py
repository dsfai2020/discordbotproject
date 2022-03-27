import os
import discord
import random
import pandas
import pickle

from dotenv import load_dotenv



load_dotenv()
TOKEN=os.getenv('DISCORD_TOKEN')
GUILD=os.getenv('DISCORD_GUILD')

#This is the client Object
client=discord.Client()

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

    elif message.content == 'trekdr':
        await message.channel.send(getcsv[["Names", "KDR"]].sort_values(by='KDR', ascending=False))

    elif message.content == 'trescore':
        await message.channel.send(getcsv[["Names", "Avg Score"]].sort_values(by='Avg Score', ascending=False))
    
    elif message.content == 'trekills':
        await message.channel.send(getcsv[['Names', 'Kills']].sort_values(by='Kills', ascending=False))
    
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


# @client.event
# async def on_message(message):
    # if 'happy birthday' in message.content.lower():
        # await message.channel.send('Happy Birthday!')

# Use postional arguments in lists to access the list without any brackets.
client.run(TOKEN)