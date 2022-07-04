import discord
import requests
import json
from discord.ext import commands

class covid(commands.Cog):
  def __init__(self,client):
    self.client = client 

  @commands.command()
  async def get_world_coivd(self,ctx):
    embed = discord.Embed(title="正在獲取新冠病毒全球趨勢",description="正在獲取新冠病毒全球趨勢的相關訊息中，請稍後...")
    msg = await ctx.send(embed=embed)   
    
    url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/total"    
    querystring = {"country":"Global"}
    headers = {
        'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
        'x-rapidapi-key': "3e99a92190msh101eb7e3faa43a8p13070djsn1178154416e5"
    }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    embed = discord.Embed(title="新冠病毒全球趨勢",description="以下為目前全球的新冠肺炎的相關訊息")
    embed.add_field(name="更新時間:", value=f"{data['data']['lastChecked'][:-6].replace('T', ' ')}", inline=False)
    embed.add_field(name="確診人數:", value=f"{data['data']['confirmed']}", inline=False)
    embed.add_field(name="死亡人數:", value=f"{data['data']['deaths']}", inline=False)
    await msg.edit(embed=embed)
    
def setup(client):
  client.add_cog(covid(client))