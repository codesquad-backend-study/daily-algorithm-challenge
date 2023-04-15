input = list(map(int, input().split()))
ascend = [1, 2, 3, 4, 5, 6, 7, 8]
descend = [8, 7, 6, 5, 4, 3, 2, 1]

if input == ascend:
    print('ascending')
elif input == descend:
    print('descending')
else:
    print('mixed')
