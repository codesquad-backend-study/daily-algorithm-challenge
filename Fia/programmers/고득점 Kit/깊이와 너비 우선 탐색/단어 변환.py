from collections import deque


def solution(begin, target, words):
    def compare(a, b):
        count = 0

        for i, char in enumerate(a):
            if char != b[i]:
                count += 1

        return count == 1

    candidates = deque([])

    for word in words:
        if compare(begin, word):
            candidates.append((word, 1))
            break

    visited = set([])

    while candidates:
        current, level = candidates.popleft()
        visited.add(current)

        if current == target:
            return level
            break

        for word in words:
            if compare(current, word) and word not in visited:
                candidates.append((word, level + 1))
                continue

    return 0
