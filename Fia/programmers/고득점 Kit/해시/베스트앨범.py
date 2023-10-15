def solution(genres, plays):
    total_plays = {}
    songs_by_genres = {}

    for i in range(len(genres)):
        if genres[i] not in total_plays.keys():
            total_plays[genres[i]] = 0

        total_plays[genres[i]] += plays[i]

        if genres[i] not in songs_by_genres.keys():
            songs_by_genres[genres[i]] = []

        songs_by_genres[genres[i]].append((i, plays[i]))

    ordered_genres = sorted(list(total_plays.items()), key=lambda x: x[1], reverse=True)

    best_album = []

    for genre in ordered_genres:
        ordered_songs = sorted(songs_by_genres[genre[0]], key=lambda x: ([x[1], -x[0]]), reverse=True)
        best_album.extend([song[0] for song in ordered_songs[:2]])

    return best_album
