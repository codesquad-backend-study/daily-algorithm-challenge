import collections


def solution(participant, completion):
    participant = collections.Counter(participant)
    completion = collections.Counter(completion)

    answer = participant - completion
    return list(answer.keys())[0]


solution(["leo", "kiki", "leo"], ["leo", "kiki"])
