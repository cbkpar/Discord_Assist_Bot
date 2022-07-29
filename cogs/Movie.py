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
    async def quiz(self, ctx):
      try:
        response = requests.get("http://www.cgv.co.kr/movies/")
		    response.encoding = 'utf-8'
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
    
        infos = soup.select('tr')
        
        for info in infos[1:10]:
            분류, 번호, 제목, 작성자, 작성일, 조회 = 정보.select('td')
            await ctx.send(f'```\n제목 : {제목.text}\n날짜 : {작성일.text}```\n링크 : http://www.cgv.co.kr/movies/{제목.a["href"]}\n--------------------------------------')
    except:
        await ctx.send(f'{today.month}월 {today.day}일 {today.hour}시 {today.minute}분 CGV 오류 발생')

def setup(client):
    client.add_cog(Movie(client))