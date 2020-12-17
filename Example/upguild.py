from UBPY import PostGuilds
import discord
from discord.ext import commands

class GuildCount(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.token = "UniqueBot TOKEN"
        PostGuilds.UpdateGuilds(self.bot,self.token)

def setup(bot):
    bot.add_cog(GuildCount(bot))
