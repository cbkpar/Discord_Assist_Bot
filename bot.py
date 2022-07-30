import discord, datetime, asyncio, random
from youtube_dl import YoutubeDL
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '!', help_command=None)

for filename in os.listdir('./cogs'):
    if '.py' in filename:
        filename = filename.replace('.py', '')
        client.load_extension(f"cogs.{filename}")

food = {
    "한식": ["떡볶이", "삼겹살", "김밥", "곱창", "불고기", "냉면", "칼국수", "된장찌개", "비빔밥", "김치찌개"],
    "중식": ["볶음밥", "짬뽕", "짜장면", "탕수육", "칠리새우", "냉채", "마파두부", "딤섬", "깐풍기", "동파육"],
    "양식": ["피자", "샐러드", "파스타", "스테이크", "샌드위치", "햄버거", "토스트", "바비큐", "핫도그", "리조또"],
    "일식": ["스시", "우동", "회", "오뎅", "라멘", "소바", "샤브샤브", "타코야끼", "가라아게", "가쓰오부시"]
}

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online)
  await client.change_presence(activity=discord.Game(name="비트아지트 (!help)"))
  print("봇 이름:",client.user.name,"봇 아이디:",client.user.id,"봇 버전:",discord.__version__)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!ping4"):
        await message.channel.send("pong1")

    if message.content.startswith("!help"):
        output = "```명령어 리스트\n"
        output += "!시놀로지\n"
        output += "!단계 (숫자)\n"
        output += "!문제뽑기 이름 이름/번호 번호\n"
        output += "!주사위 숫자\n"
        output += "!타이머 숫자\n"
        output += "!아이작 !던파 !메이플 !용들의왕 !카나타제로 !요시\n"
        output += "!투표 제목/항목1/항목2/항목3\n"
        output += "!음악재생 제목 !음악종료 !정지 !시작 !다음 !재생목록\n"
        output += "!점심추천\n"
        output += "!영화\n"
        output += "!퀴즈 !넌센스\n"
        output += "!날씨 (지역)"
        output += "```"
        await message.channel.send(output)

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

    if message.content.startswith("!타이머"):
        msgsplit = message.content.split(" ")
        number = int(msgsplit[1])
        if number >= 1:
          await message.channel.send(f'{message.author.mention}님 {number}초 타이머를 시작합니다.')
          await asyncio.sleep(number)
          await message.channel.send(f'{message.author.mention}님 시간이 {number}초 흘렀습니다.')
        else:
          await message.channel.send(f'1 이상의 정수를 넣어주세요!\nex) !타이머 10')

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

    if message.content.startswith("!피카츄"):
        await message.channel.send("https://youtu.be/g5fyObLtjCg?t=160")

    if message.content.startswith("!투표"):
        vote = message.content[4:].split("/")
        output = "```투표 - " + vote[0] + "\n"
        for i in range(1, len(vote)):
            output += str(i) +". " + vote[i] +"\n"
        output += "```"
        choose = await message.channel.send(f'{output}')
        if len(vote) > 1:
            await choose.add_reaction('1️⃣')
        if len(vote) > 2:
            await choose.add_reaction('2️⃣')
        if len(vote) > 3:
            await choose.add_reaction('3️⃣')
        if len(vote) > 4:
            await choose.add_reaction('4️⃣')
        if len(vote) > 5:
            await choose.add_reaction('5️⃣')
        if len(vote) > 6:
            await choose.add_reaction('6️⃣')
        if len(vote) > 7:
            await choose.add_reaction('7️⃣')
        if len(vote) > 8:
            await choose.add_reaction('8️⃣')
        if len(vote) > 9:
            await choose.add_reaction('9️⃣')
        if len(vote) > 10:
            await choose.add_reaction('🔟')
        
    if message.content.startswith("!점심추천"):
        categories = list(food.keys())
        category = random.choice(categories)
        lunch = random.choice(food[category]) 
        await message.channel.send(f"오늘 점심은 {category}, 그 중에서 {lunch} 어떠세요?")
    
    await client.process_commands(message)

client.run(os.environ['token'])
