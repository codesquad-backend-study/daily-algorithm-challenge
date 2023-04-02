def solution():
    max = 0
    idx = 0
    for i in range(1, 10):
        num = int(input())
        if max < num:
            max = num
            idx = i
    
    print(max)
    print(idx)
        
solution()