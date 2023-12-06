import discord
import asyncio
import os

def run_bot():
    disc_intent = discord.Intents.default()
    disc_intent.message_content= True
    client = discord.Client(intents=disc_intent)

    TOKEN = os.getenv('TOKEN')

    #Isabelle takes in and sends out responses
    @client.event
    async def on_message(message):

        username= str(message.author)
        user_message= str(message.content)
        channel= str(message.channel)
        
        #check client does not equal author
        if message.author  == client.user:
            return
        
        if message.content.startswith("!help"):
            response = response.request(message.content)
            await message.channel.send(response)
