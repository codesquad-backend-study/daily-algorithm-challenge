import collections


def solution(genres, plays):
    play_cnt = collections.defaultdict(int)
    dict = collections.defaultdict(list)

    for i in range(len(genres)):
        play_cnt[genres[i]] += plays[i]
        dict[genres[i]].append((plays[i], i))

    play_cnt = sorted(play_cnt.items(), key=lambda x: x[1])
    result = []
    while play_cnt:
        genre = play_cnt.pop()
        play_list = sorted(dict[genre[0]], key=lambda x: (x[0], -x[1]))
        best = []
        if len(play_list) == 1:
            best.append(play_list[0][1])
        else:
            first = play_list.pop()
            second = play_list.pop()
            best.append(first[1])
            best.append(second[1])
        result += best
    return result


solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])
