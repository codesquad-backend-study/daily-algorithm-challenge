def min_melody(songs: int, average: int):
    return (average - 1) * songs + 1


songs, average = map(int, input().split())

print(min_melody(songs, average))
