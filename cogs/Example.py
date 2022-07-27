from discord.ext import commands

class Example(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("example Cog is Ready")
        
    @commands.command(name="ping3", description = "pong출력")
        async def recommand_restaurant(self, ctx):
          embed = discord.Embed(title='', description=f'ㄹㄹㄹㄹㄹ', color=discord.Color.red())
          await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Example(client))