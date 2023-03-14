import discord
from discord.ext import commands
import random

TOKEN=''
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="+", intents=intents)

@bot.slash_command()
async def badge(ctx):
    await ctx.respond(random.randint(0, 100))

bot.run(TOKEN)