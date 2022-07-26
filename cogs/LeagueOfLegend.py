import discord
import asyncio
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

class LeagueofLegend(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("LeagueofLegend Cog is Ready")

    @commands.command(name ="롤")
    async def _lolsearch(self, ctx, *keywords):
        search_data = ' '.join(keywords)
        if search_data == "":
            await ctx.send(f'<https://www.op.gg/multisearch/kr?summoners=냄세제로,말랑코기엉덩이,갤럭시s4,팀운이너무없자나,도둥이의검,찰진고솜도치ANG,군대5급면제,무호흡노딜기,승표는메갈>')
            search_data = "도둥이의검"
        
        try:
            response = requests.get("https://op.gg/summoner/userName="+search_data, headers={'User-Agent': 'Mozilla/5.0'})
            response.encoding = 'utf-8'
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            output = "```"

            datas = soup.find('span', attrs={'class': 'summoner-name'})
            name = datas.text

            datas = soup.find('div', attrs={'class': 'team-and-rank'})
            datasplit = datas.text.split()
            output += name + " / 솔랭 " + datasplit[2] + "위 "+datasplit[3] + ")\n"

            datas = soup.findAll('div', attrs={'class': 'game'})
            dataskda = soup.findAll('div', attrs={'class': 'k-d-a'})
            for i in range(0, len(datas)) :
                data = datas[i].select('div')
                output += data[0].text +" "+data[1].text +" "+data[4].text+" (" + dataskda[i].text +")\n"
                if i == 4:
                    break
            output += "출처 : op.gg\n"
            output += "```"
            await ctx.send(f'{output}')
        except:
            await ctx.send(f'{today.month}월 {today.day}일 {today.hour}시 {today.minute}분 op.gg 오류 발생')

def setup(client):
    client.add_cog(LeagueofLegend(client))
