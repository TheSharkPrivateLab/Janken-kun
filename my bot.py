import discord
import asyncio
from discord.ext import commands
from random import *

description = ":arrow_forward: Bot par **Miki**\n\nTapez !help pour plus d'aide."

bot = commands.Bot(command_prefix='!', description=description)
bot.remove_command("help")

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command(pass_context=True)
async def help():
	await bot.say(':arrow_right:    -    **!roll** : Lance un dé'
		'\n:arrow_right:    -    **!help** : Affiche l\'aide'
		'\n:arrow_right:    -    **!janken** : Pierre feuille ciseaux.'
		'\n:arrow_right:    -    **!desc** : Description du bot.'
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
        await bot.say("Veuillez rentrer sous la forme de <region> <pseudo> | "
        	"Region: br, eune, euw, global, kr, lan, las, na , oce, pbe, ru, tr")

@lol.command()
async def euw(*, player: str):
	if player is None:
		await bot.say("Veuillez rentrer sous la forme de <region> <pseudo> | "
        	"Region: br, eune, euw, global, kr, lan, las, na , oce, pbe, ru, tr")
		return
	msg = await bot.say("test...")
	asyncio.sleep(2)
	await bot.edit_message(msg, "YOLO !")


bot.run('MjUxMzExMzQ4NDcyODcyOTYw.CxjrEA.0WJPDeKkVIrNJFImveaRfbU2U4w')