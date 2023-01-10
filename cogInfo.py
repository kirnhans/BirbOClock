'''''''''
Under construction.
'''''''''

import asyncio
import discord
from discord.ext import commands

class InfoCog(commands.Cog, name="Informational Commands"):

	def __init__(self, bot):
		self.bot = bot

	# pins - Reports number of pins in the channel
	@commands.command(description="Reports the number of pins in the channel in which it is called.",
	 aliases=["pin","pinned"])
	async def pins(self, ctx):
		pins = str(len(await ctx.channel.pins()))
		await ctx.send("There are " + pins + "/50 pins in this channel.")

def setup(bot):
	bot.add_cog(InfoCog(bot))