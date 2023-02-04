import discord
from discord.ext import commands
import models.sheet as sheet
from track import track, info


color_err = 0xff3333
color_success = 0x00ff00

format_list = [1, 2, 3, 4, 6]
tier_list = ['x', 's', 'a', 'ab', 'b', 'bc', 'c', 'cd', 'd', 'de', 'e', 'ef', 'f', 'fg', 'g', 'sq']

def set_record(ctx: commands.Context, args: list[str]) -> discord.Embed:
    embed_err = discord.Embed(
        title = 'Input Error', 
        description = '`.s format tier track rank`',
        color = color_err
    )

    # expected args: [track, rank, format, tier]
    if len(args) != 4:
        return embed_err
    
    # rank must be int
    if not args[3].isdecimal():
        return embed_err

    # rank must be 1~12
    if int(args[3]) <= 0 or int(args[3]) >= 13:
        return embed_err

    if int(args[0]) not in format_list:
        return embed_err

    if args[1].lower() not in tier_list:
        return embed_err

    track_id = track.track_to_id(args[2])
    rank = int(args[3])
    formt = int(args[0])
    tier = args[1].lower()

    if track_id == -1:
        return embed_err

    status, _ = sheet.set_record(track_id, rank, formt, tier, author=ctx.author)

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


def show_avg_rank(ctx: commands.Context, args: list[str]) -> list[discord.Embed]:
    embed_err = discord.Embed(
        title = 'Input Error', 
        description = '`.avgrank`',
        color = color_err
    )

    # コマンドライン引数が入力されなかったら全てのコースの平均順位を表示
    if len(args) == 0:
        return show_avg_rank_all_track(ctx)
    
    else:
        return [embed_err]

def show_avg_rank_all_track(ctx: commands.Context) -> list[discord.Embed]:
    # spreadsheetから取得
    _, track_list, rank_list = sheet.show_record(ctx.author)

    if len(track_list) == 0:
        return [discord.Embed(title = 'No Record', color = color_err)]

    # コースごとの平均順位を計算
    avg_rank_per_track, cnt_per_track = track.calculate_avg_rank_per_track(track_list, rank_list)
    avg_rank_per_track_sort = sorted(avg_rank_per_track.items(), key=lambda x:x[1])

    embed_list = [discord.Embed(title='Avarage Rank [Tracks Played]', color=color_success)]

    i = 0
    for (track_id, avg_rank) in avg_rank_per_track_sort:
        idx_list = i // 25
        # embedのfieldは25個までしか追加できないので、embedを追加
        if (i % 25 == 0) and (i != 0):
            embed_list.append(discord.Embed(title='Avarage Rank [Tracks Played]', color=color_success))
        track_name = info.TRACKS[track_id][0]
        embed_list[idx_list].add_field(name=track_name, value=f'{round(avg_rank, 2)}  [{cnt_per_track[track_id]}]')
        i += 1
    
    return embed_list



def show_avg_score(ctx: commands.Context, args: list[str]) -> list[discord.Embed]:
    embed_err = discord.Embed(
        title = 'Input Error', 
        description = '`.avgscore`',
        color = color_err
    )

    # コマンドライン引数が入力されなかったら全てのコースの平均順位を表示
    if len(args) == 0:
        return show_avg_score_all_track(ctx)
    else:
        return [embed_err]


def show_avg_score_all_track(ctx: commands.Context) -> list[discord.Embed]:
    # spreadsheetから取得
    _, track_list, rank_list = sheet.show_record(ctx.author)

    if len(track_list) == 0:
        return [discord.Embed(title = 'No Record', color = color_err)]
    
    avg_score_per_track, cnt_per_track = track.calculate_avg_score_per_track(track_list, rank_list)
    avg_score_per_track_sort = sorted(avg_score_per_track.items(), key=lambda x:x[1], reverse=True)

    embed_list = [discord.Embed(title='Avarage Score [Tracks Played]', color=color_success)]

    i = 0
    for (track_id, avg_rank) in avg_score_per_track_sort:
        idx_list = i // 25
        # embedのfieldは25個までしか追加できないので、embedを追加
        if (i % 25 == 0) and (i != 0):
            embed_list.append(discord.Embed(title='Avarage Score [Tracks Played]', color=color_success))
        track_name = info.TRACKS[track_id][0]
        embed_list[idx_list].add_field(name=track_name, value=f'{round(avg_rank, 2)}  [{cnt_per_track[track_id]}]')
        i += 1
    
    return embed_list


def count_record(ctx: commands.Context, args: list[str]) -> discord.Embed:
    embed_err = discord.Embed(
        title = 'Input Error', 
        description = '`.cnt`',
        color = color_err
    )

    # コマンドライン引数が入力されなかったら全てのコースのプレイ回数を表示
    if len(args) == 0:
        return show_all_track_count_record(ctx)
    
    else:
        return embed_err

def show_all_track_count_record(ctx: commands.Context) -> discord.Embed:
    # spreadsheetから取得
    _, track_list = sheet.show_all_track_count_record(ctx.author)

    if len(track_list) == 0:
        return discord.Embed(title = 'No Record', color = color_err)

    # コースごとの回数を計算
    cnt_per_track = track.count_per_track(track_list)
    cnt_per_track_sort = sorted(cnt_per_track.items(), key=lambda x:x[1], reverse=True)

    embed = discord.Embed(
		title = 'Tracks Played',
		color = color_success
	)

    for (track_id, cnt) in cnt_per_track_sort:
        track_name = info.TRACKS[track_id][0]
        embed.add_field(name=track_name, value=str(cnt))
    
    return embed


def delete_record(ctx: commands.Context) -> discord.Embed:
    code, track_id = sheet.delete_record(ctx.author)

    if code == 404:
        return discord.Embed(
        title = 'No Record', 
        color = color_err
    )

    track = info.TRACKS[int(track_id)][0]
    embed = discord.Embed(
		title = 'Delete Successful',
        description = track,
		color = color_success
	)
    return embed