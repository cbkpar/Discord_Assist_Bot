from discord.ext import commands

class Example(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("example Cog is Ready")
        
    @commands.event
      async def on_message(message):
      if message.content.startswith("!ping3"):
          await message.channel.send("pong3")

def setup(client):
    client.add_cog(Example(client))