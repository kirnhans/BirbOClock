'''''''''
The very most basic commands:
	ping
	hello
	sleep
'''''''''

import discord
from discord.ext import commands

class BasicCog(commands.Cog, name='Basic Commands'):
	
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command(name='ping', description="A very basic command.", brief="The most basic command.")
	async def ping(self, ctx):
		await ctx.send('pong')

def setup(bot):
	bot.add_cog(BasicCog(bot))