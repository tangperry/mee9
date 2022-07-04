#import
import discord
from discord.ext import commands 
# from reportbutton import reportbutton
# from rankcard import Rank

intents = discord.Intents.all()
client = commands.Bot(command_prefix="e!",intents=intents,help_command=None)
client.load_extension("help_cog")
client.load_extension("music_cog")
client.load_extension("covid19")
client.load_extension("rankcard")
# client.load_extension("reportmodal")

@client.event
async def on_ready():
    print(f'logged! {client.user}')

#welcome message
@client.event
async def on_member_join(member):
  channel = client.get_channel(992311262530773055)
  embed = discord.Embed(title="歡迎訊息", description=(f"歡迎 {member.mention}"),color=0x11ff00)
  await channel.send(embed=embed)

@client.command()
async def ping(ctx):
  embed = discord.Embed(title="ping", description=f"> {round(client.latency*1000)}ms")
  await ctx.send(embed=embed)


#---kick---
@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, user: discord.Member = None, *, reason: str = None): 
  if user == None:
    await ctx.send(f":x:{ctx.author.mention}你沒有指定成員")
    return
  elif reason == None:
    await user.kick()
    await ctx.send(f"**{user}** 已被{ctx.author}踢出 **沒原因**.")
    print(f"{ctx.author} use e!kick ")
  else:
    await user.kick(reason=reason)
    await ctx.send(f"**{user}** 已被{ctx.author}踢出 原因:**{reason}**.")
    print(f"{ctx.author} use e!kick ")
  
#---ban---
@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, user: discord.Member = None, *, reason: str = None):
  if user == None:
    await ctx.send(f":x:{ctx.author.mention}你沒有指定成員")
    return
  if reason == None:
    await user.ban()
    await ctx.send(f"**{user}** 已被{ctx.author}停權 **沒原因**.")
    print(f"{ctx.author} use e!ban ")
  else:
    await user.ban(reason=reason)
    await ctx.send(f"**{user}** 已被{ctx.author}停權 原因:**{reason}**.")
    print(f"{ctx.author} use e!ban ")
    
#clear messgae
#@client.command()
  #async def clear(self, ctx, num: int):
  #await ctx.chennel.purge(limit=num)
  #embed = discord.Embed(title="清除訊息", description=(f"{member.mention} "))
  #await channel.send(embed=embed)
    
@client.event
async def on_command_error(ctx,error):
  if isinstance(error, commands.CommandNotFound):
    embed=discord.Embed(title=":x:未知指令", description=(f"{error}"), color=0xff0000)
    embed.add_field(name="請使用'e!help'獲取指令", value="如果你覺得不是你的問題\n可以輸入e!report回報", inline=False)
    embed.set_footer(text=f"命令使用者:{ctx.author}",icon_url=ctx.author.avatar)
    await ctx.send(embed=embed)
  elif isinstance(error, commands.MissingRequiredArgument):
    embed=discord.Embed(title=":x:格式錯誤", description=(f"{error}"), color=0xff0000)
    embed.add_field(name="請使用'e!help'獲取指令使用方法", value="如果你覺得不是你的問題\n可以輸入e!report回報", inline=False)
    embed.set_footer(text=f"命令使用者:{ctx.author}",icon_url=ctx.author.avatar)
    await ctx.send(embed=embed)
  elif isinstance(error, commands.MissingPermissions):
    embed=discord.Embed(title=":x:存取被拒", description=(f"{error}"), color=0xff0000)
    embed.add_field(name="沒有權限使用此指令", value=f"如果你覺得不是你的問題\n可以輸入e!report回報", inline=False)
    embed.set_footer(text=f"命令使用者:{ctx.author}",icon_url=ctx.author.avatar)
    await ctx.send(embed=embed)
  else:
    embed=discord.Embed(title=":x:發生意外錯誤", description=(f"{error}"), color=0xff0000)
    embed.add_field(name=f"請檢查指令是否有異常的地方", value="如果你覺得不是你的問題\n可以輸入e!report回報", inline=False)
    embed.set_footer(text=f"命令使用者:{ctx.author}",icon_url=ctx.author.avatar)
    await ctx.send(embed=embed)

#say
@client.command()
async def say(ctx, *,msg):
  await ctx.message.delete()
  await ctx.send(msg)
  print(f"{ctx.author} use e!say ")



client.run('OTkyNzUxODcyNDc1Njc2NzAz.Gjf68L.9hDdqRFeYtSqby4N_GQfvDTGfsjF0RgnjnRIy4')