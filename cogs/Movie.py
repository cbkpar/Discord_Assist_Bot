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
        try:
            response = requests.get("http://www.cgv.co.kr/movies/")
            response.encoding = 'utf-8'
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            tags = soup.findAll('div', attrs={'class': 'box-contents'})
            output = "```"
            for i in range(0, len(tags)) :
                output += str(i+1)+". "
                output += tags[i].strong.text
                output += " " + tags[i].find("strong","percent").span.text
                output += " " + tags[i].find("span","txt-info").strong.text.split('\n')[1].replace(" ","") + "\n"
            output += "출처 : <http://www.cgv.co.kr/movies/>\n"
            output += "```"
            await ctx.send(f'{output}')
        except:
            await ctx.send(f'{today.month}월 {today.day}일 {today.hour}시 {today.minute}분 CGV 오류 발생')

def setup(client):
    client.add_cog(Movie(client))