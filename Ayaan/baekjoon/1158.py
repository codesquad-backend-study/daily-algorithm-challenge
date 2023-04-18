def solution():
    N, K = map(int, input().split())
    circle = [i for i in range(1, N+1)]
    
    result = []
    idx = 0
    while len(circle) > 0:
        # K-1 번째를 반복해서 지우는데
        # circle의 길이보다 클 경우 길이로 나눈 나머지를 idx로 지운다.
        idx += K - 1
        if idx >= len(circle):
            idx %= len(circle)
        result.append(circle[idx])
        circle.pop(idx)
    
    print("<", end="")
    print(*result, sep=", ", end="")
    print(">")
    
solution()