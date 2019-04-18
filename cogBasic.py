'''''''''
The very most basic commands:
	ping
	hello
'''''''''

import asyncio
import discord
from discord.ext import commands
import random

class BasicCog(commands.Cog, name='Basic Commands'):
	
	def __init__(self, bot):
		self.bot = bot
	
	# ping - A very basic command
	@commands.command(description="A very basic command.", brief="A very basic command.")
	async def ping(self, ctx):
		await self.bot.change_presence(activity=discord.Game(name="ping-pong"))
		await ctx.send('pong')
		await asyncio.sleep(5)

	@commands.command(description="If you ever need a friend, birbfez is here to provide.", brief="For sh*ts and giggles.")
	async def hello(self, ctx):
		msg = ["Henllo {0.message.author.mention}!!", 
		"I\N{CLAPPING HANDS SIGN}DONT\N{CLAPPING HANDS SIGN}HAEV\N{CLAPPING HANDS SIGN}HANDS\N{CLAPPING HANDS SIGN}",
		"┏┓\n" +
		"┃┃╱╲ \n" +
		"┃╱╱╲╲ in\n" +
		"╱╱╭╮╲╲this\n" +
		"▔▏┗┛▕▔  house\n" +
		"╱▔▔▔▔▔▔▔▔▔▔╲ \n" +
		"THERE IS NO DYING >:U\n" +
		"╱╱┏┳┓╭╮┏┳┓ ╲╲ \n" +
		"▔▏┗┻┛┃┃┗┻┛▕▔",
		]
		await ctx.send(msg[random.randint(0,len(msg)-1)].format(ctx))

	# consider moving into a new cog (cogMemes)
	@commands.command(description="Format your own \"in this house\" meme!", brief="there is no dying.", rest_is_raw=True)
	async def inthishouse(self, ctx, *, message:str):
		house = "...\n┏┓\n┃┃╱╲ \n┃╱╱╲╲ in\n╱╱╭╮╲╲this\n▔▏┗┛▕▔  house\n╱▔▔▔▔▔▔▔▔▔▔╲ \n" + message + "\n╱╱┏┳┓╭╮┏┳┓ ╲╲ \n▔▏┗┻┛┃┃┗┻┛▕▔"
		await ctx.send(house)

def setup(bot):
	bot.add_cog(BasicCog(bot))