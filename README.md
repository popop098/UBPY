# UBPY
# 이 레포는 UniqueBot 파이썬 **비공식** SDK입니다.

### 현재는 길드수업데이트 모듈만 존재합니다

Using Cogs
```py
import PostGuilds
import discord
from discord.ext import commands

class GuildCount(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjcyODgyMDc4ODI3ODMyOTQyNCIsImlhdCI6MTYwNzc3NDY5NywiZXhwIjozMzE0Mzc3NDY5N30.Q4ie3GmcsJk67tZr2BmLWeYulr9wKqiE_QGHd-4bTRE"
        PostGuilds.UpdateGuilds(self.bot,self.token)

def setup(bot):
    bot.add_cog(GuildCount(bot))
```
