import discord
import asyncio
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
        self.playqueue = []

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
        keyword = ' '.join(keywords)
        url = getUrl(keyword)
        await ctx.send(url)

        data = self.DL.extract_info(url, download = False)
        
        self.playqueue.append(data)

        def play_next(ctx):
            if len(self.playqueue) >= 1:
                playdata = self.playqueue.pop(0)
                link = playdata['url']
                title = playdata['title']
                ffmpeg_options = {
                    'options': '-vn',
                    "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"
                }
                player = discord.FFmpegPCMAudio(link, **ffmpeg_options)
                ctx.voice_client.play(player, after=lambda e: play_next(ctx))
            else:
                asyncio.sleep(90) #wait 1 minute and 30 seconds
                if not vc.is_playing():
                    asyncio.run_coroutine_threadsafe(vc.disconnect(ctx), self.bot.loop)
                    asyncio.run_coroutine_threadsafe(ctx.send("No more songs in queue."))

        if ctx.voice_client.is_playing():
            embed = discord.Embed(title = f'{data['title']}', description = '다음 재생 목록에 추가했어요.' , color = discord.Color.blue())
            await ctx.send(embed=embed)
        else:
          playdata = self.playqueue.pop(0)
          link = playdata['url']
          title = playdata['title']
          ffmpeg_options = {
              'options': '-vn',
              "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"
          }
          embed = discord.Embed(title = '음악 재생', description = '음악 재생을 준비하고있어요. 잠시만 기다려 주세요!' , color = discord.Color.red())
          await ctx.send(embed=embed)
          player = discord.FFmpegPCMAudio(link, **ffmpeg_options)
          ctx.voice_client.play(player, after=lambda e: play_next(ctx))
          embed = discord.Embed(title = '음악 재생', description = f'{title} 재생을 시작힐게요!' , color = discord.Color.blue())
          await ctx.send(embed=embed)

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
        if voice.is_playing() :
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

    @commands.command(name="재생목록")
    async def resume_music(self, ctx):
      embed = discord.Embed(title='플레이리스트', description='재생목록입니다', color=discord.Color.purple())
      for i in range(len(self.playqueue)):
        playdata = self.playqueue[i]
        link = playdata['url']
        title = playdata['title']
        embed.add_field(name=f'{i}.', value=f'{title}', inline=False)
      await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Music(client))