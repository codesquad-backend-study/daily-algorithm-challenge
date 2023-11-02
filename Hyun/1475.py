import collections

s = input().replace("6", "9")               # 9와 6은 호환 가능하므로 하나로 통
numbers = sorted(list(map(int, s)))         # 9가 뒤로 가게 하기 위해 정렬

counter = collections.Counter(numbers)
most = counter.most_common()[0]             # 가장 숫자가 많이 나온 숫자의 튜플을 꺼냄 (숫자, 횟수)

if most[0] == 9:                            # 숫자가 9인 경우 9와 6이 호환 가능하므로 나누기 사용
    print(most[1] // 2 + most[1] % 2)
else:
    print(most[1])
