import discord
import asyncio
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

class Baekjoon(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.problemlist = []
        self.problemlist.append(0)
        self.problemsize = 0
        response = requests.get("https://www.acmicpc.net/step")
        response.encoding = 'utf-8'
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        for a in soup.table.find_all('a', href=True):
            self.problemsize += 1
            self.problemlist.append(int(a['href'].split('/')[2]))

    @commands.Cog.listener()
    async def on_ready(self):
        print("Movie Cog is Ready")

    @commands.command(name ="단계")
    async def _step(self, ctx, args = None):
        if args == None:
            try:
                response = requests.get("https://www.acmicpc.net/step")
                response.encoding = 'utf-8'
                html = response.text
                soup = BeautifulSoup(html, 'html.parser')
                tags = soup.table.select('td')
                output = "```"
                for i in range(0,len(tags)) :
                    if i%6 == 0:
                        output += tags[i].text + ". "
                    if i%6 == 1:
                        output += tags[i].text + " : "
                    if i%6 == 2:
                        output += tags[i].text + "\n"
                    if i%120 == 119:
                        output += "```"
                        await ctx.send(f'{output}')
                        output = "```"
                output += "출처 : https://www.acmicpc.net/step/\n"
                output += "```"
                await ctx.send(f'{output}')
            except:
                await ctx.send(f'{today.month}월 {today.day}일 {today.hour}시 {today.minute}분 백준 Step 오류 발생')
        else:
            number = int(args)
            if number >= 1 and number <= self.problemsize:
                try:
                    response = requests.get("https://www.acmicpc.net/step/" + str(self.problemlist[number]))
                    response.encoding = 'utf-8'
                    html = response.text
                    soup = BeautifulSoup(html, 'html.parser')
                    tags = soup.table.select('td')
                    output = "```"
                    problem = ""
                    for i in range(0,len(tags)) :
                        if i%8 == 0:
                            output += tags[i].text + ". "
                        if i%8 == 1:
                            output += tags[i].text + " : "
                            problem += tags[i].text + " "
                        if i%8 == 2:
                            output += tags[i].text + "\n"
                        if i%160 == 159:
                            output += "```"
                            await ctx.send(f'{output}')
                            output = "```"
                    output += problem + "\n"
                    output += "```"
                    await ctx.send(f'{output}')
                except:
                    await ctx.send(f'{today.month}월 {today.day}일 {today.hour}시 {today.minute}분 백준 Step 오류 발생')
            else:
                await ctx.send(f'범위가 잘못 되었습니다')


    

def setup(client):
    client.add_cog(Baekjoon(client))