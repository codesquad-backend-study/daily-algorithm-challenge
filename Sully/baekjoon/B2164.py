import collections


def solution(card_count: int) -> int:
    queue = collections.deque()

    # 카드 초기화
    for i in range(1, card_count + 1):
        queue.append(i)

    # 한 장 남을 때까지 반복
    while True:
        if len(queue) == 1:
            break

        queue.popleft()
        queue.append(queue.popleft())

    return queue.pop()


N = int(input())
print(solution(N))
