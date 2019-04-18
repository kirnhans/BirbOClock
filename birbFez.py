import asyncio
import discord
from discord.ext import commands
import re
import random

TOKEN = 'MzM4MDc5MzU5NjczODI3MzI5.XKaguA.x02mZO1c59_dDCradPhfBFDbWrg'
BOT_PREFIX = ('f#', 'f!')
DESCRIPT = 'A work in progress. Mostly just reacts to its name.'

class MyBot(discord.Client):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		# running background tasks
		self.bg_task = self.loop.create_task(self.loop_games())

	async def on_ready(self):
		print('Logged in as ' + self.user.name + "#" + str(self.user.id))
		print('-------')

	# speak of the birbfez and it shall appear
	async def on_message(self, message):
		if message.author == self.user:
			return
		if re.search('birbfez', message.content, re.IGNORECASE):
			print('{0.author.name}#{0.author.id} mentioned birbfez in #{0.channel.name} ({0.guild.name})'.format(message))
			print("-------")
			emoji = ['\N{EYES}', '\N{THUMBS UP SIGN}', '\N{HATCHING CHICK}', '\N{BIRD}']
			mojinum = len(emoji) - 1
			await message.add_reaction(emoji[random.randint(0,mojinum)])
			return

	# background tasks:
	# loop_games(self) -> cycle through preset game statuses
	async def loop_games(self):
		await self.wait_until_ready()
		games = ["without supervision", "with humans", "Python 3", ]
		while not self.is_closed():
			try:
				for game in games:
					print('Playing ' + game)
					print("-------")
					await self.change_presence(activity=discord.Game(name=game))
					await asyncio.sleep(5)	# changes game every 5 seconds
			except:
				print('birbfez experienced a gaming mishap.')


bot = MyBot()
bot.run(TOKEN)

# bot = commands.Bot(command_prefix=BOT_PREFIX, description=DESCRIPT)
# bot.load_extension('cogBasic')

# @bot.event
# async def on_ready():
# 	print('Logged in as ' + bot.user.name + '#' + str(bot.user.id))
# 	print('-------')

# @bot.event
# async def on_message(message):
# 	# do not reply to itself
# 	if message.author == bot.user:
# 		return
# 	if re.search('birbfez', message.content, re.IGNORECASE):
# 		print('{0.author.name}#{0.author.id} mentioned birbfez in #{0.channel.name} ({0.guild.name})'.format(message))
# 		print("-------")
# 		emoji = ['\N{EYES}', '\N{THUMBS UP SIGN}', '\N{HATCHING CHICK}', '\N{BIRD}']
# 		mojinum = len(emoji) - 1
# 		await message.add_reaction(emoji[random.randint(0,mojinum)])
# 	if message.content.startswith('!shinidab'):
# 		msg = 'https://cdnw.nickpic.host/mgKajb.gif'.format(message)
# 		await message.channel.send(msg)
# 	await bot.process_commands(message)


# '''''''''
# The very most basic commands:
# 	ping
# 	hello
# 	sleep
# '''''''''

# @bot.command(name='ping', description="The most basic command... for now.", brief="The most basic command... for now.", pass_context=True)
# async def ping(ctx):
# 	print('pinged by {0.message.author.name}#{0.message.author.id}'.format(ctx))
# 	print("-------")
# 	await ctx.channel.send('pong')
# 	await bot.change_presence(activity=discord.Game(name="ping-pong"))
# 	await asyncio.sleep(5)
	
# @bot.command(name='hello', description="Almost as basic as ping.", brief="Almost as basic as ping.", pass_context=True)
# async def hello(ctx):
# 	print('{0.message.author.name}#{0.message.author.id} said hello'.format(ctx))
# 	print("-------")
# 	await ctx.channel.send('Hi, {0.message.author.mention}.'.format(ctx))

# @bot.command(name='sleep', description="It is bed o'clock.\nYou best be sleeping.", brief="It is bed o'clock.", pass_context=True)
# async def sleep(ctx):
# 	print('{0.message.author.name}#{0.message.author.id} needs to go to sleep'.format(ctx))
# 	print("-------")
# 	await ctx.channel.send('https://cdn.discordapp.com/attachments/187641780420739073/497663328337002498/1.png')


# '''''''''
# Some background tasks.
# 	list_servers
# 	loop_games
# '''''''''

# async def list_servers():
# 	await bot.wait_until_ready()
# 	channel = bot.get_channel(563660295373848607)
# 	while not bot.is_closed:
# 		print("Current servers:")
# 		for server in bot.guilds:
# 			await channel.send(guilds.name)
# 		print("-------")
# 		await asyncio.sleep(600)