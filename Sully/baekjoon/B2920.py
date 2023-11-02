words = list(map(int, input().split()))

is_ascending = -1
is_mixed = -1

# 무조건 오름차순이거나 mixed
if words[0] + 1 == words[1]:
    for i in range(len(words) - 1):
        if words[i] + 1 == words[i + 1]:
            is_ascending = 1
        else:
            is_mixed = 1
            is_ascending = -1
            break
# 무조건 내림차순이거나 mixed
elif words[0] - 1 == words[1]:
    for i in range(len(words) - 1):
        if words[i] - 1 == words[i + 1]:
            is_ascending = 0
        else:
            is_mixed = 1
            is_ascending = -1
            break
else:  # mixed
    is_ascending = -1
    is_mixed = 1

if is_ascending == 1:
    print('ascending')
elif is_ascending == 0:
    print('descending')
elif is_mixed == 1:
    print('mixed')
