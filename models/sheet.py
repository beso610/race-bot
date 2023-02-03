import os
import discord
import gspread
import datetime

from oauth2client.service_account import ServiceAccountCredentials 

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

credential = {
                "type": "service_account",
                "project_id": os.environ['SHEET_PROJECT_ID'],
                "private_key_id": os.environ['SHEET_PRIVATE_KEY_ID'],
                "private_key": os.environ['SHEET_PRIVATE_KEY'],
                "client_email": os.environ['SHEET_CLIENT_EMAIL'],
                "client_id": os.environ['SHEET_CLIENT_ID'],
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                "client_x509_cert_url":  os.environ['SHEET_CLIENT_X509_CERT_URL']
             }

credentials = ServiceAccountCredentials.from_json_keyfile_dict(credential, scope)
gc = gspread.authorize(credentials)
sh = gc.open('race bot')

TRACK_COL = 1
RANK_COL = 2
FORMAT_COL = 3
TIER_COL = 4
TIME_COL = 5

def set_record(
    track_id: int,
    rank: int,
    formt: int,
    tier: str,
    author: discord.member.Member) -> int:

    # discord idでworksheetを検索
    # 見つからなければ追加し、ユーザ名も保存しておく
    try:
        worksheet = sh.worksheet(str(author.id))
    except gspread.exceptions.WorksheetNotFound:
        worksheet = sh.add_worksheet(title=str(author.id), rows=100, cols=20)
        worksheet.update('T1', str(author))

    # 列のデータを取得し、最下行のidxを求める
    track_list = worksheet.col_values(TRACK_COL)
    last_track_idx = len(track_list)
    
    # 100行に達するごとに100行追加
    if (last_track_idx % 100 == 0) and (last_track_idx != 0):
        worksheet.add_rows(100)
    
    last_track_idx += 1

    # TODO: idxの値が全て同じであることを確認したい

    cell_list = worksheet.range('A{}:E{}'.format(last_track_idx, last_track_idx))

    cell_list[TRACK_COL-1].value = track_id
    cell_list[RANK_COL-1].value = rank
    cell_list[FORMAT_COL-1].value = formt
    cell_list[TIER_COL-1].value = tier
    cell_list[TIME_COL-1].value = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    worksheet.update_cells(cell_list)

    return 200, None


def show_all_track_avg_record(author: discord.member.Member):
    # discord idでworksheetを検索
    # 見つからなければ追加し、ユーザ名も保存しておく
    try:
        worksheet = sh.worksheet(str(author.id))
    except gspread.exceptions.WorksheetNotFound:
        worksheet = sh.add_worksheet(title=str(author.id), rows=100, cols=20)
        worksheet.update('T1', str(author))

    track_list = worksheet.col_values(TRACK_COL)
    rank_list = worksheet.col_values(RANK_COL)
    # format_list = worksheet.col_values(FORMAT_COL)
    # tier_list = worksheet.col_values(TIER_COL)
    # time_list = worksheet.col_values(TIME_COL)

    return 200, track_list, rank_list
