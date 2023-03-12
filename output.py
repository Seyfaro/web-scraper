from tabulate import tabulate
import discord
from discord.ext import commands

import discord
 
intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)


with open('ThisWeek.txt', 'r') as f:
    array_str = f.read()

# Convert the string representation back into a 2D array
my_array = [[elem.strip() for elem in row.split('~')] for row in array_str.split('\n')]

# Print the resulting 2D array
tableOut = tabulate(my_array, headers=['Collection Date', 'Bin Type'], tablefmt='orgtbl')
print(tableOut)

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

# Define a command to print the 2D array as a table
@bot.command()
async def print_table(ctx):
    await ctx.send(f'```{tableOut}```')

bot.run('MTA4NDQ5NzUzNDE1Nzg1Njc3MA.GKtH43.BdIm4uMNfQx77ngYKOYfT_uefkKxi7zYDy4WE0')