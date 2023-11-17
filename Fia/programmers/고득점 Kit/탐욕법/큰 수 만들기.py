def solution(number, k):
    length = len(number) - k
    biggest = [number[0]]
    deleted = 0

    for n in number[1:]:
        while biggest and deleted < k and biggest[-1] < n:  # 맨 마지막 숫자보다 큰 경우
            biggest.pop()
            deleted += 1

        biggest.append(n)

    while deleted < k and len(biggest) > length:
        biggest.pop()

    return "".join(biggest)
