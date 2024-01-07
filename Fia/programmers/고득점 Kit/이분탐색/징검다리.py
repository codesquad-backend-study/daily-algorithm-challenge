def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)

    left = 1
    right = distance

    answer = 0

    while left <= right:
        removed = 0
        min_gap = float('inf')

        current = 0
        mid = (left + right) // 2

        for rock in rocks:
            if removed > n:
                break

            gap = rock - current

            if mid > gap:
                removed += 1
            else:
                min_gap = min(min_gap, gap)
                current = rock

        if removed <= n:
            answer = min_gap
            left = mid + 1
        else:
            right = mid - 1

    return answer
