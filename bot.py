import os
import discord
from discord.ext import commands
from controller import record

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command(aliases=['s', 'S'])
async def set(ctx, *args):
    """1レースごとの記録を登録する"""
    await ctx.send(embed=record.set_record(ctx, args))

bot.run('DISCORD_BOT_TOKEN')