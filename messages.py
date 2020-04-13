import discord
import ffmpeg
import random
import pandas as pd
from listy import d, p
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.command()
async def test(ctx):
    await ctx.send("test")