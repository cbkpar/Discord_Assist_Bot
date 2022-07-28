import asyncio
import discord
from discord.ext import commands
import json
import random

class Quiz(commands.Cog):
    def __init__(self, client):
        self.client = client
        with open("./data/quiz.json", 'r', encoding='utf-8') as f:
            self.quizDict = json.load(f)

    @commands.Cog.listener()
    async def on_ready(self):
        print("Quiz Cog is Ready")

    @commands.command(name ="퀴즈")
    async def quiz(self, ctx):
        problemList = list(self.quizDict.keys())
        problem = random.choice(problemList)
        answer = self.quizDict[problem]
        await ctx.send(problem)

        def checkAnswer(message):
            if message.channel == ctx.channel and answer in message.content:
                return True
            else:
                return False
        try:
            await self.client.wait_for("message", timeout = 10.0, check = checkAnswer)
            await ctx.send("정답이에요!")
        except asyncio.TimeoutError:
            await ctx.send("땡! 시간초과에요!")

def setup(client):
    client.add_cog(Quiz(client))