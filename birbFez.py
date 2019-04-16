import asyncio
import re
import random

import discord
from discord import Game
from discord.ext import commands

BOT_PREFIX = ('f#', 'f!')
TOKEN = 'MzM4MDc5MzU5NjczODI3MzI5.XKaguA.x02mZO1c59_dDCradPhfBFDbWrg'
DESCRIPT = 'A work in progress. Mostly just reacts to its name.'

bot = commands.Bot(command_prefix=BOT_PREFIX, description=DESCRIPT)
bot.load_extension('cogBasic')

@bot.event
async def on_ready():
	print('Logged in as ' + bot.user.name + '#' + str(bot.user.id))
	print('-------')

@bot.event
async def on_message(message):
	# do not reply to itself
	if message.author == bot.user:
		return
	if re.search('birbfez', message.content, re.IGNORECASE):
		print('{0.author.name}#{0.author.id} mentioned birbfez in #{0.channel.name} ({0.guild.name})'.format(message))
		print("-------")
		emoji = ['\N{EYES}', '\N{THUMBS UP SIGN}', '\N{HATCHING CHICK}', '\N{BIRD}']
		mojinum = len(emoji) - 1
		await message.add_reaction(emoji[random.randint(0,mojinum)])
	if message.content.startswith('!shinidab'):
		msg = 'https://cdnw.nickpic.host/mgKajb.gif'.format(message)
		await message.channel.send(msg)
	await bot.process_commands(message)


'''''''''
The very most basic commands:
	ping
	hello
	sleep
'''''''''

@bot.command(name='ping', description="The most basic command... for now.", brief="The most basic command... for now.", pass_context=True)
async def ping(ctx):
	print('pinged by {0.message.author.name}#{0.message.author.id}'.format(ctx))
	print("-------")
	await ctx.channel.send('pong')
	await bot.change_presence(activity=discord.Game(name="ping-pong"))
	await asyncio.sleep(5)
	
@bot.command(name='hello', description="Almost as basic as ping.", brief="Almost as basic as ping.", pass_context=True)
async def hello(ctx):
	print('{0.message.author.name}#{0.message.author.id} said hello'.format(ctx))
	print("-------")
	await ctx.channel.send('Hi, {0.message.author.mention}.'.format(ctx))

@bot.command(name='sleep', description="It is bed o'clock.\nYou best be sleeping.", brief="It is bed o'clock.", pass_context=True)
async def sleep(ctx):
	print('{0.message.author.name}#{0.message.author.id} needs to go to sleep'.format(ctx))
	print("-------")
	await ctx.channel.send('https://cdn.discordapp.com/attachments/187641780420739073/497663328337002498/1.png')


'''''''''
Some background tasks.
	list_servers
	loop_games
'''''''''

async def list_servers():
	await bot.wait_until_ready()
	channel = bot.get_channel(563660295373848607)
	while not bot.is_closed:
		print("Current servers:")
		for server in bot.guilds:
			await channel.send(guilds.name)
		print("-------")
		await asyncio.sleep(600)

async def loop_games():
	await bot.wait_until_ready()
	activities = ["without supervision", "death-defying marital bliss", "with the code", "with humans"]
	while not bot.is_closed:
		for n in range(len(activities)):
			try:
				await bot.change_presence(activity=discord.GameGame(name=activities[n]))
			except:
				print("Websocket weirdness.")
			await asyncio.sleep(5)

bot.loop.create_task(list_servers())
bot.loop.create_task(loop_games())
bot.run(TOKEN, bot=True, reconnect=True)