import collections

for _ in range(int(input())):
    n = int(input())
    clothes = collections.defaultdict(int)
    for _ in range(n):
        input_data = input().split()
        clothes[input_data[1]] += 1
    result = 1
    # 조합론?
    # (종류1 + 1) * (종류2 + 1) * (종류3 + 1) ... - 1 로 구할 수 있다?
    # 생각도 못했다?
    for num in clothes.values():
        result *= (num + 1)
    print(result - 1)
