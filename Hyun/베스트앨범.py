# 노래가 가장 많이 재생된 장르 우선
# 장르 내에서 많이 재생된 노래가 먼저
# 장르 내에서 고유 번호가 작을수록 먼저
# genres 문자열, play 정수배열
# 베스트 앨범에 노래 고유번호 순서대로 return

import collections


def solution(genres, plays):
    genre_rank = collections.defaultdict(int)
    genre_dict = collections.defaultdict(list)

    for idx, genre in enumerate(genres):
        genre_rank[genre] += plays[idx]
        genre_dict[genre].append((idx, plays[idx]))

    genre_rank = sorted(genre_rank.items(), key=lambda x: x[1], reverse=True)

    best_album = []

    for genre, _ in genre_rank:
        songs_with_play_count = sorted(genre_dict[genre], key=lambda x: (-x[1], x[0]))[:2]
        songs = [x[0] for x in songs_with_play_count]
        best_album.extend(songs)

    return best_album
