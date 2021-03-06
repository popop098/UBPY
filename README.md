# UBPY
# UniqueBots 파이썬 **비공식** SDK입니다.
# 공식 SDK- 출시되었습니다. [URL](<https://github.com/decave27/uniquebots-py-sdk>)
### SaidBySolo님의 KoreanBots비공식 sdk레포의 일부를 사용해 제작되었습니다. [URL](<https://github.com/SaidBySolo/DBKR-API-Python>)

### 현재는 길드수업데이트, 투표여부 모듈만 존재합니다, 
### 길드수업데이트 모듈은 자동으로 30분마다 자동으로 길드수를 비교해 요청을 보냅니다.

### 파이썬 3.6이상을 필요로 합니다.

```
pip install UBPY --upgrade
```

## 길드 수 업데이트

**Use not Cogs**
```py
import discord
from discord.ext import commands
import UBPY
bot = commands.Bot(command_prefix='!')
#or
bot = discord.Client()

UBPY.Client(bot,token='UniqueBots TOKEN',bot_id="BOT ID")

@bot.event
async def on_ready():
    print(f"{bot.user.name} 준비 완료.")

bot.run('Discord TOKEN')
```

**Using Cogs**
```py
import UBPY
import discord
from discord.ext import commands

class GuildCount(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.token = "UniqueBots TOKEN"
        self.id = "Bot ID"
        UBPY.Client(self.bot,self.token,self.id)

def setup(bot):
    bot.add_cog(GuildCount(bot))
```

## 유저 봇 투표여부

**Cogs**
```py
import UBPY
import discord
from discord.ext import commands

class CheckVote(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.token = "UniqueBots TOKEN"
        self.id = "Bot ID"

    @commands.command(name="투표확인")
    async def _checkvote(self,ctx):
        VOTE = UBPY.UBPYvote(ctx, self.token, bot_id=self.id)
        check = await VOTE.vote()
        if check == True:
            print('TRUE')
        elif check == False:
            print('FALSE')
        else:
            print('ERROR')

def setup(bot):
    bot.add_cog(CheckVote(bot))
```

## 검색

**cogs**
```py
import UBPY
import discord
from discord.ext import commands

class Search(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.token = "UniqueBots TOKEN"

    @commands.command(name="봇리스트")
    async def _searchlist(self,ctx,page=1):
        """
        리스트에서 불러올수있는 봇정보:
        tag, heartCount, discordVerified, guilds, id, 
        status, brief, avatar, prefix, invite, locked, library, description
        """
        ser = UBPY.UBPYsearch(self.token)
        res = await ser.List(page)
        if res == False:
            print('error')
        else:
            for i in res:
                print(i["tag"])

    @commands.command(name="봇검색")
    async def _searchbot(self,ctx,ID):
        """
        불러올수있는 봇정보:
        tag, heartCount, discordVerified, guilds, id, 
        status, brief, avatar, prefix, invite, locked, library, description
        """
        ser = UBPY.UBPYsearch(self.token)
        res = await ser.search(ID=ID)
        if res == False:
            print('error')
        else:
            print(res["tag"])

    @commands.command(name="유저검색")
    async def _searchuser(self,ctx,ID,page=1):
        """
        불러올수있는 봇정보:
        tag, heartCount, discordVerified, guilds, id, 
        status, brief, avatar, prefix, invite, locked, library, description
        """
        ser = UBPY.UBPYsearch(self.token)
        res = await ser.searchuser(ID=ID,page)
        if res == False:
            print('error')
        else:
            for i in res:
                print(i["tag"])


def setup(bot):
    bot.add_cog(Search(bot))
```
