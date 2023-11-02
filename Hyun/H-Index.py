def solution(citations):
    citations.sort()
    h_index = 0
    for idx, num in enumerate(citations):
        h_index = max(h_index, min(len(citations) - idx, num))

    return h_index
