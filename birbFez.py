import asyncio
import discord
from discord.ext import commands
import re
import random

TOKEN = "MzM4MDc5MzU5NjczODI3MzI5.XKaguA.x02mZO1c59_dDCradPhfBFDbWrg"
BOT_PREFIX = ("f#", "f!")
DESCRIPT = "A work in progress. Mostly just reacts to its name."



class MyBot(commands.Bot):

	async def on_ready(self):
		print("Logged in as " + self.user.name + "#" + str(self.user.id))
		print("-------")
		cogs = ["cogBasic", "cogInfo", ]
		while not self.is_closed():
			try:
				for cog in cogs:
					self.load_extension(cog)
					print("Loaded " + cog)
				break
			except:
				print("Error loading a cog")
				print("-------")
				await asyncio.sleep(10)
		print("-------")
		self.bg_task = self.loop.create_task(self.loop_games())

	# SPEAK OF THE BIRBFEZ AND IT SHALL APPEAR
	# reacts to its name
	# tells people with certain roles to go to sleep
	async def on_message(self, message):
		if message.author == self.user:
			return
		# if message.content.startswith("test"):
		# 	await message.add_reaction("\N{PENSIVE FACE}")
		if re.search("birbfez", message.content, re.IGNORECASE):
			print("{0.author.name}#{0.author.id} mentioned birbfez in #{0.channel.name} ({0.guild.name})".format(message))
			print("-------")
			emoji = ["\N{EYES}", "\N{THUMBS UP SIGN}", "\N{HATCHING CHICK}", "\N{BIRD}", 
			"\N{BREAD}"]
			mojinum = len(emoji) - 1
			await message.add_reaction(emoji[random.randint(0,mojinum)])
		if "sleepy" in [r.name for r in message.author.roles]:
			print("{0.author.name}#{0.author.id} is still awake in #{0.channel.name} ({0.guild.name})".format(message))
			print("-------")
			msg = await message.channel.send("{0.author.mention}".format(message), file=discord.File("images/sleep.png"))
			await asyncio.sleep(5)
			await msg.delete()
		await self.process_commands(message)

	# background tasks:
	# loop_games(self) -> cycle through preset game statuses
	async def loop_games(self):
		await self.wait_until_ready()
		games = [ "without supervision", 
		# "under supervision", 
		"with humans", 
		"Python 3", 
		"The SevEn Birbly Sins: murder",
		"4 HOTT CHEETOZ"]
		while not self.is_closed():
			try:
				for game in games:
					print("Playing " + game)
					print("-------")
					await self.change_presence(activity=discord.Game(name=game))
					await asyncio.sleep(7)	# changes game every 7 seconds
			except:
				print("birbfez experienced a gaming mishap.")
				print("-------")
				await asyncio.sleep(7)

	# error handling
	async def on_command_error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.trigger_typing()
			print("{0.author.name} in {0.guild.name} was missing some arguments in the command:\n{0.message.content}".format(ctx))
			print("-------")
			await ctx.send("**{0.author.name}**, you missed some arguments in the command:\n{0.message.content}".format(ctx))



bot = MyBot(BOT_PREFIX)
bot.run(TOKEN)


'''''''''
scrapped code follows
'''''''''

# @bot.event
# async def on_message(message):
# 	# do not reply to itself
# 	if message.author == bot.user:
# 		return
# 	if message.content.startswith("!shinidab"):
# 		msg = "https://cdnw.nickpic.host/mgKajb.gif".format(message)
# 		await message.channel.send(msg)
# 	await bot.process_commands(message)


# "
# Some background tasks.
# 	list_servers
# 	loop_games
# "

# async def list_servers():
# 	await bot.wait_until_ready()
# 	channel = bot.get_channel(563660295373848607)
# 	while not bot.is_closed:
# 		print("Current servers:")
# 		for server in bot.guilds:
# 			await channel.send(guilds.name)
# 		print("-------")
# 		await asyncio.sleep(600)