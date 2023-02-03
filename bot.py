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


@bot.command(aliases=['showavg', 'sa'])
async def show_avg(ctx, *args):
    """コースの平均順位を表示する"""
    await ctx.send(embed=record.show_avg_record(ctx, args))

@bot.command(aliases=['cnt'])
async def count(ctx, *args):
    """コースごとのプレイ回数を表示する"""
    await ctx.send(embed=record.count_record(ctx, args))

bot.run(os.environ['DISCORD_BOT_TOKEN'])