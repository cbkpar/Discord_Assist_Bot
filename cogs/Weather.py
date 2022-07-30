import discord
import asyncio
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

class Weather(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Movie Cog is Ready")

    @commands.command(name ="날씨")
    async def _weather(self, ctx, args = None):
        search_data = ""
        if args == None:
            search_data = "구로동"
        else:
            search_data = str(args)
        
        try:
            response = requests.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query="+search_data+"날씨")
            response.encoding = 'utf-8'
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            output = "```"
            output += search_data+" 날씨 검색결과 입니다\n"
            tags = soup.findAll('div', attrs={'class': 'temperature_info'})
            output += tags[0].text + "\n"

            data_Time = []
            data_Weather = []
            data_Temp = []
            data_RainRatio = []
            data_RainAmount = []
            
            weathers = soup.findAll('div', attrs={'class': '_hourly_weather'})
            weather = weathers[0].select('li')
            for i in range(0,len(weather)) :
                weathersplit = weather[i].text.split()
                data_Time.append(weathersplit[0])
                data_Weather.append(weathersplit[1])
                data_Temp.append(weathersplit[2])

            rains = soup.findAll('div', attrs={'class': 'icon_wrap'})
            rain = rains[0].select('li')
            for i in range(0,len(rain)) :
                rainsplit = rain[i].text.split()
                data_RainRatio.append(rainsplit[0])
                
            rains = soup.findAll('div', attrs={'class': 'graph_wrap'})
            rain = rains[0].select('li')
            for i in range(0,len(rain)) :
                rainsplit = rain[i].text.split()
                data_RainAmount.append(rainsplit[0])
                
            for i in range(0,len(data_Time)):
                output += data_Time[i] + " - "
                output += data_Temp[i] + " "
                output += data_Weather[i] + "("+data_RainRatio[i]+") "
                output += " 강수량 : " + data_RainAmount[i] + " \n"
                if i == 19:
                    break
            output += "출처 : 네이버 날씨\n"
            output += "```"
            await ctx.send(f'{output}')
        except:
            await ctx.send(f'{today.month}월 {today.day}일 {today.hour}시 {today.minute}분 네이버 날씨 오류 발생')

def setup(client):
    client.add_cog(Weather(client))