import sys

receipt = int(sys.stdin.readline())
n = int(sys.stdin.readline())

actual = 0

for i in range(n) :
    price,count = map(int, sys.stdin.readline().split())
    actual += (price * count)

result = 'Yes' if receipt == actual else 'No'
print(result)