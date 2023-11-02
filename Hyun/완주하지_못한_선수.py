import collections


def solution(participant, completion):
    dict = collections.defaultdict(int)

    for each in participant:
        dict[each] += 1

    for each in completion:
        dict[each] -= 1
        if dict[each] == 0:
            del dict[each]

    return list(dict.keys())[0]
