import discord
from discord.ext import commands
from controller import record

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# 1レースの記録を登録
@bot.command(aliases=['s', 'S', 'set'])
async def set_record(ctx, *args):
    await ctx.send(embed=record.set_record(ctx, args))

bot.run('MTA3MDAwNDEzMjAwMzQ1OTE1Mg.GnNidP.N6LJP8lJtsicvXR_wySrtFB8UCHOdT_f1-2ZUM')