import discord
from discord.ext import commands
import models.sheet as sheet
from track import info


color_err = 0xff3333
color_success = 0x00ff00

FORMAT_LIST = [1, 2, 3, 4, 6]
TIER_LIST = ['x', 's', 'a', 'ab', 'b', 'bc', 'c', 'cd',
             'd', 'de', 'e', 'ef', 'f', 'fg', 'g', 'sq', 'w', 't']

def delete_record(ctx: commands.Context) -> discord.Embed:
    code, track_id = sheet.delete_records(ctx.author)

    if code == 404:
        return discord.Embed(
            title='No Record',
            color=color_err
        )

    track = info.TRACKS[int(track_id)][0]
    embed = discord.Embed(
        title='Delete Successful',
        description=track,
        color=color_success
    )
    return embed
