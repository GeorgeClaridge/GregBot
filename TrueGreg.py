import random
import discord
import asyncio
from discord.ext import commands

Title =['Janitor','Crab Wrangler','Hitman','Best','Archbishop', 'Overlord', 'Baron', 'Patriarch', 'Emperor', 'Chancellor', 'Elder', 'Lord', 'Prince', 'Assistant', 'Cleric', 'Nun', 'Consul', 'Curator', 'Headman', 'Delegate', 'High Priest', 'Governor', 'Master', 'Sage', 'King', 'Administrator', 'Intern']
Job = ['Miami','Crab Wrangling','Relations', 'Warfare', 'Technology', 'Forestry', 'Communications', 'Mining', 'Agriculture', 'Purity', 'Affairs', 'Tourism', 'Scouts', 'Aviation', 'Defense', 'Fishing', 'Nations' , 'Education', 'Planning', 'Dancing']
Name = 'Greg'


NewName = (f'{Name} The {random.choice(Title)} of {random.choice(Job)}')
print(NewName)
"""
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="!", intents=intents)

@client.command(pass_context=True)
async def Greg(ctx,member: discord.Member,Name):
    NewName = (f'{Name} The {random.choice(Title)} of {random.choice(Job)}')
    await member.edit(nick=NewName)

@client.command(pass_context=True)
async def chnick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Nickname was changed for {member.mention} ')
    

"""