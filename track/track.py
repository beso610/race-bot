from track import info

# コース名をコースIDに変換
def track_to_id(track_name: str) -> int:
    # 一致するコース名を検索
    for i, track_info in enumerate(info.TRACKS):
        if track_name in track_info[1]:
            return i
    
    return -1

# コースIDをコース名に変換
def id_to_track(track_id: int) -> str:
    return info.TRACKS[track_id][0]

# コースごとの平均順位を計算
def calculate_avg_rank_per_track(track_list, rank_list):
    # key: track_id, value: sum of rank
    sum_rank_per_track = dict()

    # key: track_id, value: times of track
    cnt_rank_per_track = dict()

    # key: track_id, value: avg of track
    avg_rank_per_track = dict()

    # TODO: track_listとrank_listの大きさが違うときの処理

    for i in range(len(track_list)):
        track_id = int(track_list[i])
        rank = int(rank_list[i])
    
        if (track_id in sum_rank_per_track) and (rank != ''):
            sum_rank_per_track[track_id] += rank
            cnt_rank_per_track[track_id] += 1
        elif (track_id not in sum_rank_per_track) and (rank != ''):
            sum_rank_per_track[track_id] = rank
            cnt_rank_per_track[track_id] = 1
    
    # コースごとの平均を求める
    for track_id in sum_rank_per_track.keys():
        avg_rank_per_track[track_id] = sum_rank_per_track[track_id] / cnt_rank_per_track[track_id]
    
    return avg_rank_per_track, cnt_rank_per_track

# コースのプレイ回数をカウント
def count_per_track(track_list):
    # key: track_id, value: times of track
    cnt_rank_per_track = dict()

    for i in range(len(track_list)):
        track_id = int(track_list[i])
    
        if track_id in cnt_rank_per_track:
            cnt_rank_per_track[track_id] += 1
        elif track_id not in cnt_rank_per_track:
            cnt_rank_per_track[track_id] = 1
    
    return cnt_rank_per_track