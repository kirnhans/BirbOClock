'''''''''
The very most basic commands:
	ping
	hello
	sleep
'''''''''

import discord
from discord.ext import commands

class BasicCog(commands.Cog):
	
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command(name='pong', description="Currently broken. A very basic command, except that it has its own help category.", brief="Currently broken.", pass_context=True)
	async def pong(self, ctx):
		await self.send('ping')

def setup(bot):
	bot.add_cog(BasicCog(bot))