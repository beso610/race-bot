from track import info

score_list = [15, 12, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

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
    cnt_per_track = dict()

    # key: track_id, value: avg of track
    avg_rank_per_track = dict()

    # TODO: track_listとrank_listの大きさが違うときの処理

    for i in range(len(track_list)):
        track_id = int(track_list[i])
        rank = int(rank_list[i])
    
        if (track_id in sum_rank_per_track) and (rank != ''):
            sum_rank_per_track[track_id] += rank
            cnt_per_track[track_id] += 1
        elif (track_id not in sum_rank_per_track) and (rank != ''):
            sum_rank_per_track[track_id] = rank
            cnt_per_track[track_id] = 1
    
    # コースごとの平均を求める
    for track_id in sum_rank_per_track.keys():
        avg_rank_per_track[track_id] = sum_rank_per_track[track_id] / cnt_per_track[track_id]
    
    return avg_rank_per_track, cnt_per_track


# 条件ごとに平均順位を計算
def calculate_avg_rank_by_condition(track_id_inp, formt_inp, tier_inp, track_list, rank_list, format_list, tier_list):
    # key: track_id, value: sum of rank
    sum_rank_per_track = dict()

    # key: track_id, value: times of track
    cnt_per_track = dict()

    # key: track_id, value: avg of track
    avg_rank_per_track = dict()

    for i in range(len(track_list)):
        track_id = int(track_list[i])
        rank = int(rank_list[i])
        formt = int(format_list[i])
        tier = tier_list[i]

        # True: 取得
        get_row = True

        # 指定された値があり、かつそれが取得した値が異なる場合はその行を取得しない
        if (track_id_inp != None) and (track_id_inp != track_id):
            get_row = False
        if (formt_inp != None) and (formt_inp != formt):
            get_row = False
        if (tier_inp != None) and (tier_inp != tier):
            get_row = False
        
        if get_row:
            if (track_id in sum_rank_per_track) and (rank != ''):
                sum_rank_per_track[track_id] += rank
                cnt_per_track[track_id] += 1
            elif (track_id not in sum_rank_per_track) and (rank != ''):
                sum_rank_per_track[track_id] = rank
                cnt_per_track[track_id] = 1
        
    # コースごとの平均を求める
    for track_id in sum_rank_per_track.keys():
        avg_rank_per_track[track_id] = sum_rank_per_track[track_id] / cnt_per_track[track_id]
    
    return avg_rank_per_track, cnt_per_track



# コースごとの平均点数を計算
def calculate_avg_score_per_track(track_list, rank_list):
    # key: track_id, value: sum of score
    sum_score_per_track = dict()

    # key: track_id, value: times of track
    cnt_per_track = dict()

    # key: track_id, value: avg of score
    avg_score_per_track = dict()

    # TODO: track_listとrank_listの大きさが違うときの処理

    for i in range(len(track_list)):
        track_id = int(track_list[i])
        rank = int(rank_list[i])
        
        if (track_id in sum_score_per_track) and (rank != ''):
            sum_score_per_track[track_id] += score_list[rank-1]
            cnt_per_track[track_id] += 1
        elif (track_id not in sum_score_per_track) and (rank != ''):
            sum_score_per_track[track_id] = score_list[rank-1]
            cnt_per_track[track_id] = 1

    for track_id in sum_score_per_track.keys():
        avg_score_per_track[track_id] = sum_score_per_track[track_id] / cnt_per_track[track_id]

    return avg_score_per_track, cnt_per_track

# 条件ごとに平均点数を計算
def calculate_avg_score_by_condition(track_id_inp, formt_inp, tier_inp, track_list, rank_list, format_list, tier_list):
    # key: track_id, value: sum of score
    sum_score_per_track = dict()

    # key: track_id, value: times of track
    cnt_per_track = dict()

    # key: track_id, value: avg of score
    avg_score_per_track = dict()

    for i in range(len(track_list)):
        track_id = int(track_list[i])
        rank = int(rank_list[i])
        formt = int(format_list[i])
        tier = tier_list[i]

        # True: 取得
        get_row = True

        # 指定された値があり、かつそれが取得した値が異なる場合はその行を取得しない
        if (track_id_inp != None) and (track_id_inp != track_id):
            get_row = False
        if (formt_inp != None) and (formt_inp != formt):
            get_row = False
        if (tier_inp != None) and (tier_inp != tier):
            get_row = False
        
        if get_row:
            if (track_id in sum_score_per_track) and (rank != ''):
                sum_score_per_track[track_id] += score_list[rank-1]
                cnt_per_track[track_id] += 1
            elif (track_id not in sum_score_per_track) and (rank != ''):
                sum_score_per_track[track_id] = score_list[rank-1]
                cnt_per_track[track_id] = 1
        
    # コースごとの平均を求める
    for track_id in sum_score_per_track.keys():
        avg_score_per_track[track_id] = sum_score_per_track[track_id] / cnt_per_track[track_id]
    
    return avg_score_per_track, cnt_per_track

# コースのプレイ回数をカウント
def count(track_list):
    # key: track_id, value: times of track
    cnt_per_track = dict()

    for i in range(len(track_list)):
        track_id = int(track_list[i])
    
        if track_id in cnt_per_track:
            cnt_per_track[track_id] += 1
        elif track_id not in cnt_per_track:
            cnt_per_track[track_id] = 1
    
    return cnt_per_track

def count_by_condition(track_id_inp, formt_inp, tier_inp, track_list, rank_list, format_list, tier_list):
    # key: track_id, value: times of track
    cnt_per_track = dict()

    for i in range(len(track_list)):
        track_id = int(track_list[i])
        rank = int(rank_list[i])
        formt = int(format_list[i])
        tier = tier_list[i]

        # True: 取得
        get_row = True

        # 指定された値があり、かつそれが取得した値が異なる場合はその行を取得しない
        if (track_id_inp != None) and (track_id_inp != track_id):
            get_row = False
        if (formt_inp != None) and (formt_inp != formt):
            get_row = False
        if (tier_inp != None) and (tier_inp != tier):
            get_row = False
        
        if get_row:
            if (track_id in cnt_per_track) and (rank != ''):
                cnt_per_track[track_id] += 1
            elif (track_id not in cnt_per_track) and (rank != ''):
                cnt_per_track[track_id] = 1
        
    return cnt_per_track