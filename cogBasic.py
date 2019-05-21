'''''''''
The very most basic commands:
	ping
	hello
	inthishouse
	sleepy
'''''''''

import asyncio
import discord
from discord.ext import commands
import random

class BasicCog(commands.Cog, name='Basic Commands'):
	
	def __init__(self, bot):
		self.bot = bot
	
	# ping - Tests connection
	@commands.command(description="A very basic command.", brief="A very basic command.")
	async def ping(self, ctx):
		await self.bot.change_presence(activity=discord.Game(name="ping-pong"))
		await ctx.send('pong')
		await asyncio.sleep(5)

	# hello - Replies with one of several random strings
	@commands.command(description="If you ever need a friend, birbfez is here to provide.", brief="For sh*ts and giggles.")
	async def hello(self, ctx):
		msg = ["Henllo {0.message.author.mention}!!", 
		#"I\N{CLAPPING HANDS SIGN}DONT\N{CLAPPING HANDS SIGN}HAEV\N{CLAPPING HANDS SIGN}HANDS\N{CLAPPING HANDS SIGN}",
		"{0.message.author.mention}\n" +
		"┏┓\n" +
		"┃┃╱╲ \n" +
		"┃╱╱╲╲ in\n" +
		"╱╱╭╮╲╲this\n" +
		"▔▏┗┛▕▔  house\n" +
		"╱▔▔▔▔▔▔▔▔▔▔╲ \n" +
		"\N{SPARKLES}PLz 2B MAKE USELLF @ HOEM!!\N{SPARKLES}\n" +
		"╱╱┏┳┓╭╮┏┳┓ ╲╲ \n" +
		"▔▏┗┻┛┃┃┗┻┛▕▔",
		]
		await ctx.send(msg[random.randint(0,len(msg)-1)].format(ctx))

	# inthishouse - sends the "in this house" meme
	# consider moving into a new cog (cogMemes)
	@commands.command(description="Format your own \"in this house\" meme!", brief="there is no dying.")
	async def inthishouse(self, ctx, *, message:str):
		# try:
		house = "...\n┏┓\n┃┃╱╲ \n┃╱╱╲╲ in\n╱╱╭╮╲╲this\n▔▏┗┛▕▔  house\n╱▔▔▔▔▔▔▔▔▔▔╲ \n" + message + "\n╱╱┏┳┓╭╮┏┳┓ ╲╲ \n▔▏┗┻┛┃┃┗┻┛▕▔"
		await ctx.send(house)
		# except commands.MissingRequiredArgument:
		# 	def acheck(m):
		# 		return m.author == ctx.author
		# 	await ctx.send("In this house what?")
		# 	try:
		# 		msg = await self.bot.wait_for("message", timeout=30.0, check=acheck)
		# 		house = "...\n┏┓\n┃┃╱╲ \n┃╱╱╲╲ in\n╱╱╭╮╲╲this\n▔▏┗┛▕▔  house\n╱▔▔▔▔▔▔▔▔▔▔╲ \n" + msg + "\n╱╱┏┳┓╭╮┏┳┓ ╲╲ \n▔▏┗┻┛┃┃┗┻┛▕▔"
		# 		await ctx.send(house)
		# 	except asyncio.TimeoutError:
		# 		house = "...\n┏┓\n┃┃╱╲ \n┃╱╱╲╲ in\n╱╱╭╮╲╲this\n▔▏┗┛▕▔  house\n╱▔▔▔▔▔▔▔▔▔▔╲ \n**birbfez is the besst!!**\n╱╱┏┳┓╭╮┏┳┓ ╲╲ \n▔▏┗┻┛┃┃┗┻┛▕▔"
		# 		await ctx.send(house)


	# sleepy group of commands:
	# role - sets the role within the guild to be used as the sleepy role
	# sleepy - adds the sleepy role to the member mentioned,
	#	or asks who to make sleepy.
	@commands.group(description="Under construction.", brief="Something about sleep?")
	async def sleepy(self, ctx, arg:str):
		# if ctx.invoked_subcommand is None:
			# await ctx.send("**{0.author.name}**, the correct usage is ``f!sleepy [ @user | role ]``".format(ctx))

		def rcheck():
			return "sleepy" in [r.name for r in ctx.guild.roles]
		if not rcheck():
			await ctx.send("There is no sleepy role.")

		try:
			await ctx.send(arg + " is now sleepy".format(ctx))
		except Forbidden:
			await ctx.send("I don't have permission to add roles \N{PENSIVE FACE}")
		except:
			def acheck(m):
				return m.author == ctx.author
			await ctx.send("Who's sleepy?")
			try:
				msg = await self.bot.wait_for("message", timeout=30.0, check=acheck)
				await ctx.send(msg.content + " is sleepy.")
			except asyncio.TimeoutError:
				await ctx.send("Guess nobirby's sleepy then. \N{BLACK SUN WITH RAYS}")

	# # wakeup - removes the sleepy role from the member mentioned
	# @commands.command(description="Removes the sleepy role.", brief="No longer sleepy.")
	# async def wakeup(self, ctx):
	# 	role = await create_role(ctx.guild.roles, name="sleepy")
	# 	await member.remove_roles([role])


def setup(bot):
	bot.add_cog(BasicCog(bot))