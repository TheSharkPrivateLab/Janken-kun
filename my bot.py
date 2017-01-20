import discord
import asyncio
from discord.ext import commands
from random import *

description = ":arrow_forward: Bot par **Miki**\n\nTapez !help pour plus d'aide."

bot = commands.Bot(command_prefix='!', description=description)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def aide():
	await bot.say(':arrow_right:  -  !roll : lance un dé\n:arrow_right:  -  !help : affiche l\'aide\n:arrow_right:  -  !janken : pierre feuille ciseaux.\n\n C\'EST TOUT POUR LE MOMENT !!')

@bot.command()
async def roll():
    """Rolls a dice in NdN format."""
    try:
        await bot.say(':game_die: {} :game_die:'.format(round(random() * 100)))
    except Exception:
        await bot.say('Error !')
        return

@bot.command()
async def janken():
	tmp = randint(0, 10)
	if tmp >= 0 and tmp <= 2:
		await client.send_message(message.channel, ':scissors:')
	elif tmp >= 3 and tmp <= 5:
		await client.send_message(message.channel, ':punch:')
	else:
		await client.send_message(message.channel, ':raised_hand:')
		
			#await client.send_message(message.channel, ':game_die: {} :game_die:'.format(round(random() * 100)))



bot.run('MjUxMzExMzQ4NDcyODcyOTYw.CxjrEA.0WJPDeKkVIrNJFImveaRfbU2U4w')