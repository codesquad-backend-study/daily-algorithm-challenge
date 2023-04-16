X = int(input())
N = int(input())
is_X = 0
for i in range(N):
    a, b = map(int, input().split())
    is_X += a * b

if X == is_X:
    print("Yes")
else:
    print("No")