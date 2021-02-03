import discord
from discord.ext import commands

def is_admin():
    def chk(ctx):
        return ctx.message.author.id == 702361652812578856
    return commands.check(chk)
