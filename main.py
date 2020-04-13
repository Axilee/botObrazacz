import os
import random
import discord
import ffmpeg
import subprocess
import messages
from dotenv import load_dotenv
from discord.ext import commands
from discord import FFmpegPCMAudio
from discord.utils import get
import time
import pandas as pd
from listy import d, p

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print(f'{client.user.name+" "} has connected to Discord!')

@client.command(aliases=["cześć", "cz"],pass_context = True)
async def cos(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    source = FFmpegPCMAudio('mp3\\czesc.mp3')
    player = voice.play(source)
    server = ctx.message.guild.voice_client
    time.sleep(0.5)
    await server.disconnect()
  
        
@client.command(aliases=["kurwa", "ku"],pass_context = True)
async def kur(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    source = FFmpegPCMAudio('mp3\\kurwa.mp3')
    l = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', 'mp3\\kurwa.mp3'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    dlugosc = float(l.stdout)
    player = voice.play(source)
    server = ctx.message.guild.voice_client
    time.sleep(dlugosc)
    await server.disconnect()
   

@client.command(aliases=["b"],pass_context = True)
async def baumel(ctx,arg):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("Wejdź do kanału głosowego")
        return
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        
    plik = f"mp3\\{arg}.mp3"
    source = FFmpegPCMAudio(plik)
    l = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', plik], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    dlugosc = float(l.stdout)
    player = voice.play(source)
    server = ctx.message.guild.voice_client
    time.sleep(dlugosc)
    await server.disconnect()


@client.command()
async def lista(ctx):
    lista = ""
    for file in os.listdir("C:\\Users\\kacpe\\Desktop\\DiscordBot\\v2\\mp3"):
        if file.endswith(".mp3"):
            t = file.split(".",1)[0]
            lista+=f"{t}\n"
    
    await ctx.send(lista)

@client.command(pass_context = True)
async def rand(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("Wejdź do kanału głosowego")
        return
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    lista = []
    for file in os.listdir("C:\\Users\\kacpe\\Desktop\\DiscordBot\\v2\\mp3"):
        if file.endswith(".mp3"):
            lista.append(file)
    plik = random.choice(lista)
    sciezka = f"mp3\\{plik}"
    source = FFmpegPCMAudio(sciezka)
    l = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', sciezka], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    dlugosc = float(l.stdout)
    player = voice.play(source)
    server = ctx.message.guild.voice_client
    time.sleep(dlugosc)
    await server.disconnect()
rand = random.choice
imiona = pd.read_csv("csv//zenskie.csv")
rarity = ['common: ','uncommon: ','rare!: ', "EPIC!: ", 'LEGENDARYYYYY: ']
@client.command()
async def XD(ctx):
     response = random.choice(d)
     await ctx.send(response)




@client.command()
async def dodaj(ctx):
    wiad = message.content.split("!dodaj ",1)[1]
    wiad = random.choice(rarity) + wiad 
    d.append(wiad)

@client.command()
async def komendy(ctx):
    h = '`!lista` - lista mp3 do !baumel\n`!baumel "<nazwa mp3 z !list>"` - baumel coś powie (musi być w cudzysłowiu jezeli zawiera spacje)\n`!czesc,!cz` - baumel sie przywita\n`!kurwa,!ku` - baumel sie wkurwi\n`!rand` - randomowy baumel'
    await ctx.send(h)

client.run(TOKEN)
