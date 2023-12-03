def solution(numbers, target):
    global count
    count = 0

    def sum(idx, total):
        if idx >= len(numbers):
            if total == target:
                global count
                count += 1
            return

        sum(idx + 1, total + numbers[idx])
        sum(idx + 1, total - numbers[idx])

    sum(0, 0)

    return count
