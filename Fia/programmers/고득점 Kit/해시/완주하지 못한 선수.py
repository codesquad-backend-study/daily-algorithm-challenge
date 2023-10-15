from collections import Counter


def solution(participant, completion):
    rest = Counter(participant) - Counter(completion)

    return list(rest.keys())[0]
