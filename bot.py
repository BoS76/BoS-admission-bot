# bot.py
import os
import sys

from dotenv import load_dotenv

project_home = '/home/BoS76/webhook'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

load_dotenv(os.path.join(project_home, '.env'))
TOKEN = os.getenv('DISCORD_TOKEN')

print(TOKEN)
