import discord
import asyncio
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

class Movie(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Movie Cog is Ready")

    @commands.command(name ="영화")
    async def _movie(self, ctx):
        await ctx.send('movie test!')


def setup(client):
    client.add_cog(Movie(client))