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