import discord
from discord.ext import commands
import random
import os

client = commands.Bot(command_prefix = '/')

@client.event
async def on_ready():

  await client.change_presence(status=discord.Status.online)
  await client.change_presence(activity=discord.Game(name="비트아지트"))
  print("봇 이름:",client.user.name,"봇 아이디:",client.user.id,"봇 버전:",discord.__version__)

@client.event
async def on_message(message):
    if message.content.startswith("!ping"):
        await message.channel.send("pong4")

    if message.content.startswith("!시놀로지"):
        await message.channel.send("시놀로지 : <http://jusin.synology.me:5000/>")

    if message.content.startswith("!문제뽑기"):
        info = message.content[6:]
        infosplit = info.split("/")
        people = infosplit[0]
        problems = infosplit[1]
        person = people.split(" ")
        problem = problems.split(" ")
        random.shuffle(problem)
        output = ""
        for i in range(0, len(person)):
          output += str(i+1) + ". " + person[i] + " : " + problem[i] + "번 (<https://www.acmicpc.net/problem/" + problem[i] + ">)\n"
        await message.channel.send(f'{output}')
        
    if message.content.startswith("!주사위"):
        msgsplit = message.content.split(" ")
        number = int(msgsplit[1])
        if number >= 2:
          await message.channel.send(f'주사위를 굴려 {random.randint(1,number)}이(가) 나왔습니다. (1-{number})')
        else:
          await message.channel.send(f'2 이상의 정수를 넣어주세요!\nex) !주사위 6')

    if message.content.startswith("!아이작"):
        await message.channel.send("https://youtu.be/g5fyObLtjCg")

    if message.content.startswith("!던파"):
        await message.channel.send("https://youtu.be/kEvlmInotpU")

    if message.content.startswith("!메이플"):
        await message.channel.send("https://youtu.be/7iqHOJ-7LNY")

    if message.content.startswith("!용들의왕"):
        await message.channel.send("https://youtu.be/E-FCy8zKDD4")

    if message.content.startswith("!카타나제로"):
        await message.channel.send("https://youtu.be/GbzeaAkcL9g")

    if message.content.startswith("!요시"):
        await message.channel.send("https://youtu.be/v_hWPGw070w")

client.run(os.environ['token'])