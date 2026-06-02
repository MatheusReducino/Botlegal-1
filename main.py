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

@bot.command()
async def somalegal(ctx, num1, num2):
    numb1 = int(num1)
    numb2 = int(num2)
    soma = numb1 + numb2
    autor = ctx.author.name
    await ctx.reply(f"oie {autor}, a soma disso ai é {soma}")

@bot.command()
async def pfp(ctx):
    pfp = ctx.author.display_avatar.url
    await ctx.reply(f"a foto do bobao ai hahaha {pfp}")

@bot.command()
async def invadecasabranca(ctx):
    casabranca = "https://lexlegal.com.br/wp-content/uploads/2025/08/trump-4.jpg"
    await ctx.send(f"Invadimos, mas o trump malvado pegou a gente {casabranca}")

bot.run("Token do teu bot")