import discord
from discord.ext import commands

class manage():
  def __init__(self,bot):
    self.bot = bot
    
  @commands.Cog.listener()
  async def on_guild_join(self,guild):
    
