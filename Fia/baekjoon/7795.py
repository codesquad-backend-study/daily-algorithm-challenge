# 먹을 것인가 먹힐 것인가

test_case = int(input())

for _ in range(test_case):
    a_count, b_count = map(int, input().split())
    a_list = [*map(int, input().split())]
    b_list = sorted([*map(int, input().split())])

    answer = 0

    for a in a_list:
        left = 0
        right = len(b_list) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if b_list[mid] >= a:
                right = mid - 1
            else:
                left = mid + 1

        answer += left

    print(answer)

