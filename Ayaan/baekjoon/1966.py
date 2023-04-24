from collections import deque

for _ in range(int(input())):
    length, target = map(int, input().split())
    importance = list(map(int, input().split()))
    importance = [[i, val] for i, val in enumerate(importance)]
    queue = deque(importance)
    
    count = 0
    while len(queue) > 0:
        # 첫번째를 빼서
        std = queue.popleft()
        isMax = True
        for element in queue:
            # 큐에 큰값이 있으면 뒤에 다시 추가
            if std[1] < element[1]:
                queue.append(std)
                isMax = False
                break
        # 가장 큰 값이면 인쇄
        if isMax:
            count += 1
            if std[0] == target:
                print(count)
                break
        