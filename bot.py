# bot.py
import os

import discord

TOKEN = '{NzMzNjk4MzI3MjExOTMzNzU3.XxG8Gg.9zZ6yIYKxV_tG6TYrK6tAmR-hh8}'

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)
