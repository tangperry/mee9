import discord
from discord.ext import commands 

class reportmodal(commands.Cog):
  def __init__(self,client):
    self.client = client 

  @commands.command()
  async def report(self):
    embed = discord.Embed(title="MEE9回報")
    embed.add_field(name="回報標題", value=self.children[0].value)
    embed.add_field(name="回報內容", value=self.children[1].value)

    button = discord.ui.Button(label="")
    await ctx.send(embed=embed)
    # await interaction.respond.send_message(embeds=[embed])
    # await interaction.response.send_modal(reportmodal(title="回報"))
    
    self.add_item(discord.ui.InputText(label="標題"))
    self.add_item(discord.ui.InputText(label="內容", style=discord.InputTextStyle.long))
    
    # async def callback(self, interaction: discord.Interaction):
        
      
    @discord.ui.button(label="回報",style=discord.ButtonStyle.primary, emoji="📋")
    async def button_callback(self, button, interaction)
