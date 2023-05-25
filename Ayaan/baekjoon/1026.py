N = int(input())
A_list = sorted(map(int, input().split()))
B_list = sorted(map(int, input().split()), reverse=True)

result = 0
for i in range(N):
    result += A_list[i] * B_list[i]
print(result)
