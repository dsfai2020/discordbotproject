import os
import discord
import random

from dotenv import load_dotenv


load_dotenv()
TOKEN=os.getenv('DISCORD_TOKEN')


client=discord.Client()

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

    squad= ["Sniper Class -- Falcon 8, Snake Eyes"]
    
    if message.content == 'trehistory':
        response = random.choice(trehistory)
        await message.channel.send(response)

    elif message.content == 'squad':
        await message.channel.send(squad[0])

# @client.event
# async def on_message(message):
    # if 'happy birthday' in message.content.lower():
        # await message.channel.send('Happy Birthday!')

client.run(TOKEN)