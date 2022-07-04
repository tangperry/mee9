import discord
from discord.ui import View,Select
from discord.ext import commands

class helpselect(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.command()
  async def help(self,ctx):
    embed = discord.Embed(title="指令列表",description="你你可以在這裡知道任何命令的使用方法!\n說明:(@user)代表要指定成員、(!*)代表可填可不填"
                          ,color=0x11ff00)

    embed1 = discord.Embed(title="工具指令",color=0x11ff00)
    embed1.add_field(name="1.e!ping", value="可以查看機器人當前的延遲狀況", inline=False)
    embed1.add_field(name="2.e!report", value="可以回報問題給製作者", inline=False)
    embed1.add_field(name="3.e!say (text)", value="可以讓機器人說出你指定的話", inline=False)
    embed1.add_field(name="4.e!get_world_coivd", value="可以獲取目前全球疫情的狀況", inline=False)
    
    embed2 = discord.Embed(title="管理員指令",color=0x11ff00)
    embed2.add_field(name="1.e!kick (@user) (!原因)", value="可以踢出指定的成員", inline=False)
    embed2.add_field(name="2.e!ban (@user) (!原因)", value="可以對指定的成員停權", inline=False)

    embed3 = discord.Embed(title="音樂指令",color=0x11ff00)
    embed3.add_field(name="1.e!m_join", value="可以讓機器人進入指令使用者的語音頻道", inline=False)
    embed3.add_field(name="2.e!m_play(不能使用) (YT_URL或音樂名)", value="可以搜尋或是指定連結撥放", inline=False)
    embed3.add_field(name="3.e!m_quit", value="可以讓機器人退出語音頻道", inline=False)
    embed3.add_field(name="4.e!m_pause", value="可以讓機器人暫停正在撥放的音樂", inline=False)
    embed3.add_field(name="5.e!m_resume", value="可以讓機器人恢復撥放已暫停的音樂", inline=False)
    embed3.add_field(name="6.e!m_(1~5)", value="可以選擇搜尋的音樂撥放", inline=False)
         
    select = Select(options=[
        discord.SelectOption(label="工具指令",
                emoji="🛠️",
                description=""),  
        discord.SelectOption(label="管理員指令",            
                emoji="👑",
                description="管理員專屬指令"),     
        discord.SelectOption(label="音樂指令",            
                emoji="🎶",
                description="讓語音頻道變成音樂廳"),
        discord.SelectOption(label="其他指令",            
                emoji="💭",
                description=""),
        ]
      )

    async def callback(interaction):
      if f"{select.values[0]}" == "工具指令":
        await interaction.response.edit_message(embed=embed1)   
      elif f"{select.values[0]}" == "管理員指令":
        await interaction.response.edit_message(embed=embed2) 
      elif f"{select.values[0]}" == "音樂指令":
        await interaction.response.edit_message(embed=embed3) 
      # elif f"{select.values[0]}" == "其他指令":
      #   await interaction.response.edit_message()
    
    select.callback = callback
    view = View()
    view.add_item(select)
    await ctx.send(embed=embed,view=view)

def setup(client):
  client.add_cog(helpselect(client))