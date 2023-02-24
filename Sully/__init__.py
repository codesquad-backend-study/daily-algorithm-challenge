n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}
result = [i for i in a if i not in remove_set]
print(result)

input1 = int(input())
data = list(map(int, input().split()))
data.sort(reverse=True)
print(data)

a1, a2, a3 = map(int, input().split())
print(a1, a2, a3)
