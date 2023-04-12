def solution():
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    result = []
    for i in range(len(data)):
        dungchi = 0
        for j in range(len(data)):
            if i == j:
                continue
            if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
                dungchi += 1
        result.append(dungchi + 1)
    
    print(*result)
    
    
solution()