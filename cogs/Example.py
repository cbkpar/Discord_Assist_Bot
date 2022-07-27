from discord.ext import commands

class Example(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("example Cog is Ready")
        
    @bot.event
    async def on_message(message):
      await bot.process_commands(message)
      await message.channel.send("pong1")


def setup(client):
    client.add_cog(Example(client))