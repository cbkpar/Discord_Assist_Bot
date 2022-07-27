import discord, datetime, asyncio, random
from youtube_dl import YoutubeDL
from discord.ext import commands
import os

class Music(commands.Cog):
    def __init__(self, client):
        option = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        }
        self.client = client
        self.DL = YoutubeDL(option)

    @commands.Cog.listener()
    async def on_ready(self):
        print("Music Cog is Ready")

    @commands.command(name = "유투브")
    async def url_reading(self, ctx, url):
        data = self.DL.extract_info(url, download = False)
        title = data['title']
        uploader = data['uploader']
        uploader_url = data['uploader_url']
        view_count = data['view_count']
        average_rating = data['average_rating']
        like_count = data['like_count']
        thumbnail=data['thumbnail']

        embed = discord.Embed(title = title, url = url)
        embed.set_author(name = uploader, url = uploader_url)
        embed.add_field(name = '조회수', value = view_count, inline = True)
        embed.add_field(name = '평점', value = average_rating, inline = True)
        embed.add_field(name = '좋아요 수', value = like_count, inline = True)
        embed.set_image(url = thumbnail)
        await ctx.send(embed = embed)

    @commands.command(name = "음악재생")
    async def play_music(self, ctx, url):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                embed = discord.Embed(title = '오류 발생', description = "음성 채널에 들어간 후 명령어를 사용해 주세요",
                color = discord.Color.red())
                await ctx.send(embed = embed)
                raise commands.CommandError("Author not connected to a voice channel.")

        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()

        await ctx.send(url)
        embed = discord.Embed(title = '음악 재생', description = '음악 재생을 준비하고 있어요. 잠시만 기다려주세요!', color = discord.Color.green())
        await ctx.send(embed = embed)
    
        data = self.DL.extract_info(url, download = False)
        link = data['url']
        title = data['title']
        uploader = data['uploader']

        ffmpeg_options = {
            'options': '-vn',
            "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"
        }
        player = discord.FFmpegPCMAudio(link, **ffmpeg_options, executable = "C:/ffmpeg/bin/ffmpeg")

        ctx.voice_client.play(player)
        embed = discord.Embed(title = f'{title}', url=url, color = discord.Color.red())
        embed.set_author(name = f'{uploader}', url = url )
        embed.add_field(name = '조회수', value=data['view_count'], inline=True)
        embed.add_field(name = '평점', value=data['average_rating'], inline=True)
        embed.add_field(name = '좋아요 수', value=data['like_count'], inline=True)
        embed.set_image(url = data['thumbnail'])
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Music(client))


client = commands.Bot(command_prefix = '/')

@client.event
async def on_ready():

  await client.change_presence(status=discord.Status.online)
  await client.change_presence(activity=discord.Game(name="비트아지트 (!help)"))
  print("봇 이름:",client.user.name,"봇 아이디:",client.user.id,"봇 버전:",discord.__version__)

@client.event
async def on_message(message):
    if message.content.startswith("!ping"):
        await message.channel.send("pong7")

    if message.content.startswith("!help"):
        output = "```명령어 리스트\n"
        output += "!시놀로지\n"
        output += "!문제뽑기 이름 이름/번호 번호\n"
        output += "!주사위 숫자\n"
        output += "!타이머 숫자\n"
        output += "!아이작\n"
        output += "!던파\n"
        output += "!메이플\n"
        output += "!용들의왕\n"
        output += "!카타나제로\n"
        output += "!요시\n"
        output += "!투표 제목/항목1/항목2/항목3\n"
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
        
client.run(os.environ['token'])