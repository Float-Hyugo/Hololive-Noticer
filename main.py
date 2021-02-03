import discord
from discord.ext import commands
import check
itt = discord.Intents.all()
bot = commands.Bot(prefix="$",intents=itt)

@bot.event
async def on_ready():
  print("ready")
  
@bot.command()
@check.is_admin()
async def load(ctx,module:str):
  try:
    bot.load_extension(module)
  except as e:
    await ctx.send(f'```\n{e}\n```)
  else:
    await ctx.messag.add_reaction('👍')
            
