import discord
import os

def run_bot():
    disc_intent = discord.Intents.default()
    disc_intent.message_content= True
    client = discord.Client(intents=disc_intent)

    TOKEN = os.getenv('TOKEN')