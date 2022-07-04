import discord
from discord.ext import commands
import youtube_dl,youtube_search

class music(commands.Cog):
  def __init__(self,client):
    self.client = client  
    self.youtube_scing = False
    self.re_name = None
    
  @commands.command()
  async def m_join(self,ctx):
      if ctx.author.voice is None:
        await ctx.send(f":x:{ctx.author}你要先進語音頻道")  
        return    
      voiceChannel = ctx.author.voice.channel
      if ctx.voice_client is None:
        embed = discord.Embed(title="正在加入",description="正在加入中，請稍後...",color=0x11ff00)
        msg = await ctx.send(embed=embed)
        await voiceChannel.connect()
        embed = discord.Embed(title="完成",description="已加入語音頻道",color=0x11ff00)
        await msg.edit(embed=embed)
  
  @commands.command()
  async def m_play(self,ctx,*,name):
      if ctx.author.voice is None:
        await ctx.send(f":x:{ctx.author}你要先進語音頻道")  
        return    
      embed = discord.Embed(title="正在加入",description="正在加入中，請稍後...",color=0x11ff00)
      msg = await ctx.send(embed=embed)
      voiceChannel = ctx.author.voice.channel
      if ctx.voice_client is None:
        await voiceChannel.connect()
      embed = discord.Embed(title="正在搜尋",description="正在搜尋中，請稍後...",color=0x11ff00)
      await msg.edit(embed=embed)
      self.youtube_scing = True
      results = youtube_search.YoutubeSearch(name, max_results=5).to_dict()
      self.re_name = [
        results[0]["title"],
        results[0]["url_suffix"],
        results[1]["title"],
        results[1]["url_suffix"],
        results[2]["title"],
        results[2]["url_suffix"],
        results[3]["title"],
        results[3]["url_suffix"],
        results[4]["title"],
        results[4]["url_suffix"]
      ]  
      embed = discord.Embed(title="Youtube搜尋結果",description="以下為搜尋結果:",color=0x11ff00)
      for i in range(0,5):
        embed.add_field(name=f"{i+1}.{results[i]['title']}", value=f"{'https://youtube.com' + results[i]['url_suffix']}", inline=False)
      await msg.edit(embed=embed)

  @commands.Cog.listener()
  async def m_play2(self,ctx,num,name):
    if self.youtube_scing:
      embed = discord.Embed(title="正在下載",description="正在下載中，請稍後...",color=0x11ff00)
      msg = await ctx.send(embed=embed)
      FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
      song_name = name[num]
      url_suffix = name[num + 1]
      url = f"https://youtube.com{url_suffix}"
      embed = discord.Embed(title="正在播放:",description = f"[{song_name}]({url})",color=0x11ff00)
      vc = ctx.voice_client
      ydl_opts = {'format': 'bestaudio'}
      with youtube_dl.YoutubeDL(ydl_opts) as ydl:
          info = ydl.extract_info(url, download=False)
          url2 = info['formats'][0]['url']
          sc = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
          try:
            vc.play(sc)
            self.youtube_sc = False
            await msg.edit(embed=embed)
          except Exception as e:
            if str(e) == "Already playing audio.":
              await ctx.send(f":x:{ctx.author}暫時無法再添加一次音樂!")
              return

  @commands.command()
  async def m_quit(self,ctx):
    if self.re_name != None:
      ctx.voice_client.disconnect()
      await ctx.send("⏏️已退出")

  @commands.command()
  async def m_pause(self,ctx):
    if self.re_name != None:
      ctx.voice_client.pause()
      await ctx.send("⏸️已暫停播放")
  
  @commands.command()
  async def m_resume(self,ctx):
    if self.re_name != None:
      ctx.voice_client.resume()
      await ctx.send("▶️已恢復播放")

  @commands.command()
  async def m_1(self,ctx):
    if self.re_name != None:
      await self.m_play2(ctx,0,self.re_name)
      self.re_name = None
    else:
      await ctx.send(f":x:{ctx.author}你還沒有搜尋音樂")
      
  @commands.command()
  async def m_2(self,ctx):
    if self.re_name != None:
      await self.m_play2(ctx,1,self.re_name)
      self.re_name = None
    else:
      await ctx.send(f":x:{ctx.author}你還沒有搜尋音樂")
      
  @commands.command()
  async def m_3(self,ctx):
    if self.re_name != None:
      await self.m_play2(ctx,2,self.re_name)
      self.re_name = None
    else:
      await ctx.send(f":x:{ctx.author}你還沒有搜尋音樂")
      
  @commands.command()
  async def m_4(self,ctx):
    if self.re_name != None:
      await self.m_play2(ctx,3,self.re_name)
      self.re_name = None
    else:
      await ctx.send(f":x:{ctx.author}你還沒有搜尋音樂")
      
  @commands.command()
  async def m_5(self,ctx):
    if self.re_name != None:
      await self.m_play2(ctx,4,self.re_name)
      self.re_name = None
    else:
      await ctx.send(f":x:{ctx.author}你還沒有搜尋音樂")

def setup(client):
  client.add_cog(music(client))