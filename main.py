import os
import discord
from discord.ext import commands
from discord.ext.commands.core import has_guild_permissions
import requests
import DiscordUtils
from discord.ext import tasks
from datetime import date
import asyncio
from keep_alive import keep_alive


intents= discord.Intents.default()
intents.members=True
client = commands.Bot(command_prefix='//', intents=intents)






from music import music



client.add_cog(music(client))


	

	

@client.event
async def on_ready():
	watching = discord.Activity(type=discord.ActivityType.watching, name=f'GÆM use //help')
	await client.change_presence(activity=watching)
	print('we have logged in as{0.user}'.format(client))
	
	
@client.event
async def on_guild_join(guild):
	for channel in guild.text_channels:
		if channel.permissions_for(guild.me).send_messages:
			guildname=guild.name
			await channel.send(f'Thank you for adding me in {guildname}  you may start by using the ``welcomemessage`` to add the channel to send the welcome me to and then the ``//help`` command to get started ')
		break	
      	
      		
	
keep_alive()
client.run('ODk4ODg1NTQ4MTA0NjM0NDIw.YWquZw.67QRMFWMiaX0IsO7AANQBSWaBow')