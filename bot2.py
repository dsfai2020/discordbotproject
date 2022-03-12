import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN=os.getenv('DISCORD_TOKEN')

class CustomClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

client=CustomClient()
client.run(TOKEN)

# This creates a client variable and calls .run() with the discord token
