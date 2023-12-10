import collections


def solution(begin, target, words):
    def count(current, word):
        cnt = 0
        for i in range(len(current)):
            if current[i] != word[i]:
                cnt += 1
        return cnt == 1

    dist = {word: -1 for word in words}

    if target not in words:
        return 0

    queue = collections.deque()
    queue.append(begin)
    dist[begin] = 0

    while queue:
        current = queue.popleft()

        for word in words:
            if dist[word] == -1:
                if count(current, word):
                    queue.append(word)
                    dist[word] = dist[current] + 1

    return dist[target] if dist[target] != 0 else 0
