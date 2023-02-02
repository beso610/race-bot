import discord
import gspread
import json
import datetime

from oauth2client.service_account import ServiceAccountCredentials 

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('race-bot-376506-13d34a4a8107.json', scope)
gc = gspread.authorize(credentials)
SPREADSHEET_KEY = '1-1IOOWTRruFo-4bIKg73asAUi5xXtruC1Qg2mqbBUYg'
sh = gc.open('race bot')


def set_record(
    track_id: int,
    rank: int,
    sheet_name: str) -> int:

    try:
        worksheet = sh.worksheet(sheet_name)
    except gspread.exceptions.WorksheetNotFound:
        worksheet = sh.add_worksheet(title=sheet_name, rows=100, cols=20)

    TRACK_COL = 1
    RANK_COL = 2
    TIME_COL = 3

    # 列のデータを取得し、最下行のidxを求める
    track_list = worksheet.col_values(TRACK_COL)
    last_track_idx = len(track_list) + 1

    # TODO: idxの値が全て同じであることを確認

    cell_list = worksheet.range('A{}:C{}'.format(last_track_idx, last_track_idx))

    cell_list[TRACK_COL-1].value = track_id
    cell_list[RANK_COL-1].value = rank
    cell_list[TIME_COL-1].value = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    worksheet.update_cells(cell_list)

    return 200