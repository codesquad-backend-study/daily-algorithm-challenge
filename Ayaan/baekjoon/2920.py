def solution():
    melody = list(map(int, input().split()))
    result = "mixed"
    # 1로 시작할 때
    if melody[0] == 1:
        result = "ascending"
        std = melody[0]
        for i in range(1, len(melody)):
            std += 1
            if std == melody[i]:
                continue
            else:
                result = "mixed"
                break
    # 8로 시작할 때
    elif melody[0] == 8:
        result = "descending"
        std = melody[0]
        for i in range(1, len(melody)):
            std -= 1
            if std == melody[i]:
                continue
            else:
                result = "mixed"
                break
    print(result)
    
solution()