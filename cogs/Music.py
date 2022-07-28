import discord
from discord.ext import commands
from youtube_dl import YoutubeDL
from .module.youtube import getUrl

class Music(commands.Cog):
    def __init__(self, client):
        option = {
            'format': 'bestaudio/best',
            'noplaylist': True,
        }
        self.client = client
        self.DL = YoutubeDL(option)
        self.TestNumber = 1

    @commands.Cog.listener()
    async def on_ready(self):
        print("Music Cog is Ready")

    @commands.command(name ="음악재생")
    async def play_music(self, ctx, *keywords):
        if ctx.voice_client is None: 
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                embed = discord.Embed(title = '오류 발생', description = "음성 채널에 들어간 후 명령어를 사용 해 주세요!", color = discord.Color.red())
                await ctx.send(embed=embed)
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()
        keyword = ' '.join(keywords)
        url = getUrl(keyword)
        await ctx.send(url)
        embed = discord.Embed(title = '음악 재생', description = '음악 재생을 준비하고있어요. 잠시만 기다려 주세요!' , color = discord.Color.red())
        await ctx.send(embed=embed)

        data = self.DL.extract_info(url, download = False)
        link = data['url']
        title = data['title']

        ffmpeg_options = {
            'options': '-vn',
            "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"
        }
        


        player = discord.FFmpegPCMAudio(link, **ffmpeg_options)
        ctx.voice_client.play(player)
        embed = discord.Embed(title = '음악 재생', description = f'{title} 재생을 시작힐게요!' , color = discord.Color.blue())
        await ctx.send(embed=embed)
        self.TestNumber += 1
        await ctx.send(f'{self.TestNumber} 입니다')
        

    @commands.command(name ="음악종료")
    async def quit_music(self, ctx):
        voice = ctx.voice_client
        if voice.is_connected():
            await voice.disconnect()
            embed = discord.Embed(title = '', description = '음악 재생을 종료합니다.' , color = discord.Color.blue())
            await ctx.send(embed=embed)

    @commands.command(name="정지")
    async def pause_music(self, ctx):
        voice = ctx.voice_client
        if voice. :
            await voice.pause()
            embed = discord.Embed(title='', description='음악 재생을 일시정지합니다.', color=discord.Color.purple())
            await ctx.send(embed=embed)

    @commands.command(name="시작")
    async def resume_music(self, ctx):
        voice = ctx.voice_client
        if voice.is_paused():
            await voice.resume()
            embed = discord.Embed(title='', description='멈춘 부분부터 음악을 재생합니다.', color=discord.Color.purple())
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Music(client))