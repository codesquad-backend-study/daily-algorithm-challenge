import collections

N, M = map(int, input().split())
deque = collections.deque([i for i in range(1, N+1)])

num_list = list(map(int, input().split()))
result = 0
for num in num_list:
    if deque[0] == num:
        deque.popleft()
    else:
        # 왼쪽으로 이동 횟수와 오른쪽 이동 횟수를 구한다.
        left_count = len(deque) - deque.index(num)
        right_count = deque.index(num)
        if left_count < right_count:
            while True:
                pop_num = deque.pop()
                result += 1
                if pop_num == num:
                    break
                deque.appendleft(pop_num)
        else:
            while True:
                pop_num = deque.popleft()
                if pop_num == num:
                    break
                result += 1
                deque.append(pop_num)
print(result)
