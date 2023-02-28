import os
import discord
from discord.ext import commands
from controller import record

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))
    await bot.change_presence(
        activity=discord.Activity(status=discord.Status.online, type=discord.ActivityType.watching,
                                  name=f"{len(bot.guilds)} servers"))


@bot.command(aliases=['s', 'S'])
async def set(ctx, *args):
    """1レースごとの記録を登録する"""
    await ctx.send(embed=record.set_record(ctx, args))


@bot.command(aliases=['avgrank', 'ar'])
async def show_avg_rank(ctx, *args):
    """コースの平均順位を表示する"""
    embed_list = record.show_avg_rank(ctx, args)
    for embed in embed_list:
        await ctx.send(embed=embed)

@bot.command(aliases=['avgscore', 'as'])
async def show_avg_score(ctx, *args):
    """コースの平均点数を表示する"""
    embed_list = record.show_avg_score(ctx, args)
    for embed in embed_list:
        await ctx.send(embed=embed)

@bot.command(aliases=['cnt'])
async def count(ctx, *args):
    """コースごとのプレイ回数を表示する"""
    await ctx.send(embed=record.count_record(ctx, args))

@bot.command(aliases=['d', 'del'])
async def delete(ctx):
    """最新の記録を削除する"""
    await ctx.send(embed=record.delete_record(ctx))

bot.run(os.environ['DISCORD_BOT_TOKEN'])