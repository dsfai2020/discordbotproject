import os
import discord
import random
import pandas

from dotenv import load_dotenv



load_dotenv()
TOKEN=os.getenv('DISCORD_TOKEN')

#This is the client Object
client=discord.Client()

#Triggers on client events
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

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

    roster= {'Falcon 8': 'Sniper', 'Rat 6': 'Flanker', 'Jaguar 9': 'Push Support'}
    
    if message.content == 'trehistory':
        response = random.choice(trehistory)
        await message.channel.send(response)

    elif message.content == 'roster':
        rosterprompt=['Which member of the TRE would you like to learn about?']
        await message.channel.send(rosterprompt[0])


    elif message.content == 'trekdr':
        await message.channel.send(df[["Names", "KDR"]])

    elif message.content == 'trescore':
        await message.channel.send(df[["Names", "Avg Score"]])

# @client.event
# async def on_message(message):
    # if 'happy birthday' in message.content.lower():
        # await message.channel.send('Happy Birthday!')

# Use postional arguments in lists to access the list without any brackets.

client.run(TOKEN)