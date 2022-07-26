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
        await message.channel.send("pong2")

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
          output += person[i] + "------------>" + problem[i] + "번 (https://www.acmicpc.net/problem/"+problem[i]+")\n"
        await message.channel.send(f'{output}')


client.run(os.environ['token'])