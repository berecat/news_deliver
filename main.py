import json
import discord 
import news
import os 
from dotenv import load_dotenv
from time import sleep
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)
news_file = "text1.json"

# @bot.event
# async def on_s

@bot.event

@bot.event
async def on_message(message):
    if message.content == "news":
        await message.channel.send("Generate News")
        with open(news_file, 'r') as f:
            data = json.load(f)
            for articles in data["articles"][:5]:
                sleep(0.1)
                await message.channel.send(articles["link"])
    elif message.content == "update":
        news.find_news()
bot.run(DISCORD_TOKEN)