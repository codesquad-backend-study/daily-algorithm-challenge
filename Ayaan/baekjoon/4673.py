def solution():
    # 0~10000까지 True인 리스트를 만든다.
    selfNum = [True for i in range(0,10001)]
    
    # 1~10000까지 d(n)을 구해서 False로 만든다.
    for i in range(1, len(selfNum)):
        d = i
        while(i != 0):
            d += i % 10
            i //= 10
        # 10000보다 큰 값은 필요없음
        if d > 10000:
            continue
        selfNum[d] = False
    
    for i in range(1, len(selfNum)):
        if selfNum[i] == True:
            print(i)
    
solution()
