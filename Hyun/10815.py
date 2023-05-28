n = int(input())
nums = list(map(int, input().split()))
nums_dic = {num: 1 for num in nums}

cnt = int(input())
given_nums = list(map(int, input().split()))

for given_num in given_nums:
    if given_num in nums_dic:
        print(1, end=" ")
    else:
        print(0, end=" ")
