def solution():
    rule = [1, 1, 2, 2, 2, 8]
    chess = list(map(int, input().split()))
    for i in range(len(chess)):
        print(rule[i] - chess[i], end=" ")
    
solution()