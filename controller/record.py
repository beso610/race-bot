import discord
from discord.ext import commands
import models.sheet as sheet
from track import track


color_err = 0xff3333
color_success = 0x00ff00

def set_record(ctx: commands.Context, args: list[str]) -> discord.Embed:
    embed_err = discord.Embed(
        title = 'Input Error', 
        description = '**Ex.** `_s ttc 12`',
        color = color_err
    )

    # expected args: [track, rank]
    if len(args) != 2:
        return embed_err
    
    # rank must be int
    if not args[1].isdecimal():
        return embed_err

    # rank must be 1~12
    if int(args[1]) <= 0 or int(args[1]) >= 13:
        return embed_err
    
    rank = int(args[1])
    track_id = track.track_to_id(args[0])

    if track_id == -1:
        return embed_err

    status = sheet.set_record(track_id, rank, sheet_name=str(ctx.author))

    if rank == 1:
        rank_description = '🥇 1st'
    elif rank == 2:
        rank_description = '🥈 2nd'
    elif rank == 3:
        rank_description = '🥉 3rd'
    else:
        rank_description = f'{rank}th'


    if status == 200:
        embed = discord.Embed(
            title = track.id_to_track(track_id),
            description = rank_description,
            color = color_success,
        )
        return embed
    
    return embed_err