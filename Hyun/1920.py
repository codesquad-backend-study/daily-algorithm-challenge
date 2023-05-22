n = int(input())
numbers = list(map(int, input().split()))
number_dic = {number: 1 for number in numbers}

m = int(input())
given_numbers = list(map(int, input().split()))
ans = []

for idx in range(m):
    if given_numbers[idx] in number_dic:
        print(1)
    else:
        print(0)
