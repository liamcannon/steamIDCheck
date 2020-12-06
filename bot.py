import discord
import os
from discord.ext.commands.bot import Bot
from discord.ext import commands
import steam_ID_Check
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


intents = discord.Intents.all()

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.command(name="checkid")
async def checkid(ctx, arg_sid):
    await ctx.send(steam_ID_Check.is_S_parent(arg_sid))
    

bot.run(TOKEN)
