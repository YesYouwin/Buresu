import discord
from discord import app_commands
from discord.ext import commands
from datetime import datetime
import os
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host="0.0.0.0", port=10000)

def keep_alive():
    t = Thread(target=run)
    t.start()
    

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)

async def setup_hook():
    await bot.load_extension("scrim")
    await bot.load_extension("player_logs") 

bot.setup_hook = setup_hook

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logged in as {bot.user}")


keep_alive()
bot.run(TOKEN)
