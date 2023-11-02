def solution():
    s = input().upper()
    # 중복을 제거한 문자들을 구해서 for문을 돌린다.
    s_set = set(s)
    
    max = 0
    result = ""
    for ch in s_set:
        count = s.count(ch)
        if count > max:
            max = count
            result = ch
        elif count == max:
            result = "?"
    print(result)
    
solution()