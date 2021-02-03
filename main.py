import discord
from discord.ext import commands
itt = discord.Intents.all()
bot = commands.Bot(prefix="$",intents=itt)

@bot.event()
async def on_ready():
  print("ready")
  
  
