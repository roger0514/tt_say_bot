import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return    

    #print(message.content)
    #print(message.channel.id)

    if message.channel.id==1029298839485689909:
        content = message.content
        await message.delete() #刪除原始訊息
        await message.channel.send(message.content) #重複訊息
        #print("try to get channel")
        #channel = client.get_channel(953194865167069195)
        #print("get channel")
        #await channel.send(message.content)
        return

client.run('MTAyOTUxMjk2NTQ5MTI2OTczNA.GKhMaU.84EX7pXYhBE1GZU36Kyo4cKwZ_mpWhycDKEnb8')
