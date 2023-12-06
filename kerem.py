import discord
import os
import random
import requests
from discord.ext import commands
import nest_asyncio
nest_asyncio.apply()


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')


@bot.command()
async def mem(ctx):
    with open('/content/TR1a7e888c7a1d59220c4a7e866c083ae8.jpg', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def oyun(ctx):
  await ctx.send(f'Oyun oynamanın bazen yararları bazen de zararları olabilir.')
   
@bot.command()
async def oyun2(ctx):
   await ctx.send(f"https://www.google.com/imgres?imgurl=https%3A%2F%2Fi.ytimg.com%2Fvi%2F0_DgN-Gwo5w%2Fmaxresdefault.jpg&tbnid=ppj9LjPqdE0dEM&vet=10CBUQMyhyahcKEwigl7G8nvuCAxUAAAAAHQAAAAAQCA..i&imgrefurl=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D0_DgN-Gwo5w&docid=ml-l2Y34drDFzM&w=1280&h=720&itg=1&q=bilgisayar%20oyunun%20zararlar%C4%B1&ved=0CBUQMyhyahcKEwigl7G8nvuCAxUAAAAAHQAAAAAQCA")



@bot.command()
async def detay_olumlu(ctx):
     with open('/content/oyunlar.jpg', 'rb') as f:
        
        picture = discord.File(f)
   
     await ctx.send(file=picture) 

@bot.command()
async def detay_olumsuz(ctx):
    resim=random.choice(os.listdir("/content/oyun"))
    with open(f'/content/oyun{resim}', 'rb') as f:
        
        picture = discord.File(f)
   
    await ctx.send(file=picture)






bot.run("")
