import discord
import asyncio
import time
from discord.ext import commands
from bin.leagueof import *
from random import *

description = ":arrow_forward: Bot par **Miki**\n\nTapez !help pour plus d'aide."

bot = commands.Bot(command_prefix='!', description=description)
bot.remove_command("help")
bot.game = discord.Game(name='Bot By Miki')
bot.lol = Lol('RGAPI-d5620781-f00e-4cc1-80cd-4a6e9289bb67', default_region=EUROPE_WEST)
bot.__mutedBaka__ = dict()

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print(str(bot.game))
	print('------')
	bot.change_status(game=bot.game)

@bot.command(pass_context=True)
async def help():
	await bot.say(':arrow_right:	-	**!roll** : Lance un dé'
		'\n:arrow_right:	-	**!help** : Affiche l\'aide'
		'\n:arrow_right:	-	**!janken** : Pierre feuille ciseaux.'
		'\n:arrow_right:	-	**!desc** : Description du bot.'
		'\n\n C\'EST TOUT POUR LE MOMENT !!')

@bot.command(pass_context=True)
async def desc():
	await bot.say(bot.description)

@bot.command(pass_context=True)
async def roll():
	"""Rolls a dice."""
	try:
		await bot.say(':game_die: {} :game_die:'.format(randint(0, 100)))
	except Exception:
		await bot.say('Error !')
		return

@bot.command(pass_context=True)
async def janken():
	tmp = randint(1, 100)
	if tmp >= 0 and tmp <= 33:
		await bot.say(':scissors:')
	elif tmp >= 34 and tmp <= 66:
		await bot.say(':punch:')
	else:
		await bot.say(':raised_hand:')

@bot.group(pass_context=True)
async def lol(ctx):
	if ctx.invoked_subcommand is None:
		await bot.say(":x: Veuillez rentrer sous la forme de <region> <pseudo> | "
			"Region: br, eune, euw, global, kr, lan, las, na , oce, pbe, ru, tr")

@lol.command()
async def euw(*players : str):

	if len(players) == 0:
		await bot.say(":x: Veuillez rentrer sous la forme de <region> <pseudo> | "
			"Region: br, eune, euw, global, kr, lan, las, na , oce, pbe, ru, tr")
		return

	player = ""
	for i in players:
		player += i
		player += " "

	msg = await bot.say(":information_source: Collection des information...")
	summoner = bot.lol.check_lol(player, EUROPE_WEST)
	if type(summoner) == type(""):
		await bot.edit_message(msg, summoner)
		return
	else:
		await bot.edit_message(msg, bot.lol.message_lol(summoner))

async def mute(message):
	temp = message.content[::-1]
	tempo = []
	timer = str()

	test = True
	a = 0

	while test:
		tempo.append(temp[a])
		if tempo[a].isnumeric() is False:
			del tempo[a]
			test = False
		a += 1

	for i in tempo:
		timer += i

	timer = int(timer[::-1])
	bot.__mutedBaka__[str(message.raw_mentions[0])] = temps + timer


@bot.event
async def on_message(message):

	temps = round(time.time())
		
	if message.author.id in bot.__mutedBaka__.keys():
		if bot.__mutedBaka__[str(message.author.id)] <= temps:
			del bot.__mutedBaka__[str(message.author.id)]
			if message.content.startswith('!mute'):
				await mute(message)
			else:
				await bot.process_commands(message)
		else:
			await bot.delete_message(message)
	else:
		if message.content.startswith('!mute'):
			await mute(message)
		else:
			await bot.process_commands(message)


bot.run('MjUxMzExMzQ4NDcyODcyOTYw.CxjrEA.0WJPDeKkVIrNJFImveaRfbU2U4w')