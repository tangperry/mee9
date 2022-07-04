import discord
from reportmodal import reportmodal 

class reportbutton(discord.ui.View): 
    @discord.ui.button(label="回報",style=discord.ButtonStyle.primary, emoji="📋")
    async def button_callback(self, button, interaction):
        await interaction.response.send_modal(reportmodal(title="回報"))

                                              

