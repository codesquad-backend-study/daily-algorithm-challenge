S = input()

# {알파벳: 처음 등장하는 위치} 딕셔너리 생성
alp_dict = {}

# 문자열을 아스키코드로 바꾸고
for i in range(ord('a'), ord('z') + 1):
    # 아스키코드를 또 문자열로 바꾸고
    # S 문자열 안에 알파벳이 존재하는 경우
    if chr(i) in S:
        # index() 메서드는 첫번째 문자를 기준
        alp_dict[chr(i)] = S.index(chr(i))
    # S 문자열 안에 알파벳이 존재하지 않는 경우
    else:
        alp_dict[chr(i)] = -1

# 값을 공백으로 구분하여 출력
# 예를 들어 [1, 2, 3] 이렇게 출력되는 게 -> 1 2 3 이런 식으로 출력됨
print(*alp_dict.values())
