import collections

t = int(input())

for _ in range(t):
    total_cnt, target_idx = map(int, input().split())

    priority = list(map(int, input().split()))              # 문서 우선순위 저장
    idxs = [idx for idx in range(total_cnt)]                # 문서 인덱스 저장, 0 1 2 3...
    priority_with_idx = collections.deque(zip(priority, idxs))              # (우선순위, 인덱스) 튜플로 큐를 만든다. 문서들을 의미

    sorted_priority = collections.deque(sorted(priority, reverse=True))     # 문서 우선순위를 내림차순으로 정렬하여 큐를 만든다.

    print_count = 1
    while True:
        if priority_with_idx[0][0] == sorted_priority[0]:                   # 맨 앞 문서의 우선순위가 현재 존재하는 최우선 순위인 경우
            if priority_with_idx[0][1] == target_idx:                           # 맨 앞 문서의 인덱스가 내가 구하고자 하는 인덱스인 경우
                break                                                           # 반복문 탈출

            sorted_priority.popleft()
            priority_with_idx.popleft()                                     # 해당 문서를 문서들에서 제거
            print_count += 1
        else:
            priority_with_idx.append(priority_with_idx.popleft())           # 우선순위가 낮은 문서인 경우, 걍 뒤로 보낸다.


    print(print_count)
