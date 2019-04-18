'''''''''
When activated, tells people to go to sleep.
'''''''''

import asyncio
import discord
from discord.ext import commands

class SleepyCog(commands.Cog, name='Time\'s a-Ticking'):

	def __init__(self, bot):
		self.bot = bot

	@bot.command(description="It is bed o'clock.\nYou best be sleeping.", brief="It is bed o'clock.")
	async def sleep(self, ctx):
		sleepy = ctx.author
		try:
			role = get(ctx.guild.roles, name="needs bedtime reminders")
		except:
			create_role(ctx.guild, name="needs bedtime reminders")
			role = get(ctx.guild.roles, name="needs bedtime reminders")
		await sleepy.add_roles(role)

def setup(bot):
	bot.add_cog(SleepyCog(bot))