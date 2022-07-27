from discord.ext import commands

class Example(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("example Cog is Ready")
        
    @commands.command(name="ping")
    async def restaurant(self, ctx):
      embed = discord.Embed(title=nowDate + ' pong.', description=descript, color=discord.Color.blue())
      await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Example(client))