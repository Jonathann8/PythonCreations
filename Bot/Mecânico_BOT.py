import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(".", intents=intents)

@bot.event
async def on_ready():
    print("Bot inicializado com sucesso!")

    @bot.command()
    async def olá(ctx):
        await ctx.reply("Olá, tudo bem?")


bot.run("MTM5Njk4NTYyNDYxOTEyMjk5Mg.GG-OK4.lGKopmnxFuTM5ukvCXtowRqvYhpNuynIvBIrAY")