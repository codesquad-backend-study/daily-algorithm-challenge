def B1152():
    s = input().split()
    print(len(s))


string = " The first character is a blank "
# B1152()


def B10809():
    s = input()
    # a~z까지 -1로 초기화
    alphabet = {chr(i + ord('a')):-1 for i in range(26)}
    
    for i in range(len(s)):
        # 첫 위치를 넣어주기 위해 -1인 경우만 
        if alphabet[s[i]] == -1:
            alphabet[s[i]] = i
    
    # list를 *로 풀어줘서 출력
    print(*alphabet.values())
    
B10809()