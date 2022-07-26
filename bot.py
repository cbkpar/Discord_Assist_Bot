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
        await message.channel.send("pong3")

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
        iCount = 1
        for i in range(0, len(person)):
          output += iCount+". " + person[i] + " : " + problem[i] + "번 (<https://www.acmicpc.net/problem/"+problem[i]+">)\n"
          iCount += 1
        await message.channel.send(f'{output}')
        
    if message.content.startswith("!주사위"):
        msgsplit = message.content.split(" ")
        number = int(msgsplit[1])
        if number >= 2:
          await message.channel.send(f'주사위를 굴려 {random.randint(1,number)}이(가) 나왔습니다. (1-{number})')
        else:
          await message.channel.send(f'2 이상의 정수를 넣어주세요!\nex) /주사위 6')

client.run(os.environ['token'])