def solution():
    T = int(input())
    for _ in range(T):
        H, W, N = map(int, input().split())
        
        room = 0
        if N % H == 0:
            room += H * 100
            room += N // H
        else:
            room += N % H * 100
            room += N // H + 1
        
        print(room)
    
solution()