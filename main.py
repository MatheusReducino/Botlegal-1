import discord
from discord.ext import commands
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    canal = bot.get_channel(id_do_canal)
    await canal.send("Puf, inicializado com sucesso")

@bot.command()
async def ping(ctx):
    await ctx.reply(f"pong, haha ganhei")
bot.run("Token do teu bot")