def solution():
    T = int(input())
    count = 0
    for _ in range(T):
        s = input()
        # 앞에서부터 붙어있는 문자를 제거했는데도
        # 뒤에 같은 문자가 남아있는지 체크
        while(len(s) > 0):
            ch = s[0]
            idx = 0
            # 0번째 부터 같은 문자들이 나오는 위치의 다음 index를 구한다.
            while(s[idx] == ch):
                idx += 1
                if idx > len(s)-1:
                    break
            # 같은 문자들을 제거
            s = s[idx:]
            # 첫번째 문자를 앞에서부터 다 제거하고 남은 문자열에 문자가 있으면 그룹 단어가 아니다.
            if s.find(ch) != -1:
                break
            if len(s) == 0:
                count += 1
    print(count)

solution()