'''''''''
Under construction.
'''''''''

import asyncio
import discord
from discord.ext import commands

class InfoCog(commands.Cog, name='Informational Commands'):

	def __init__(self, bot):
		self.bot = bot

def setup(bot):
	bot.add_cog(InfoCog(bot))