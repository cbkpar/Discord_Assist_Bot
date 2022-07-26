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
    if message.content.startswith("ping"):
        await message.channel.send("pong")

@client.event
async def on_message(message):
    if message.content.startswith("!문제뽑기"):
        info = message.content[6:]
        infosplit = info.split("/")
        people = infosplit[0]
        problems = infosplit[1]
        person = people.split(" ")
        problem = problems.split(" ")
        random.shuffle(problem)
        for i in range(0, len(person)):
          await message.channel.send(f'{person[i]} + "--------->" + {problem[i]}')

@client.command(name='주사위')
async def roll(ctx, number: int):
    await ctx.send(f'주사위를 굴려 {random.randint(1,number)}이(가) 나왔습니다. (1-{number})')

@roll.error
async def roll_error(ctx, error):
    await ctx.send(f"2 이상의 정수를 넣어주세요!\nex) /주사위 6")


client.run(os.environ['token'])