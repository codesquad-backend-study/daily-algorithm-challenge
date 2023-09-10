# 줄어들지 않아
import sys

tests = int(sys.stdin.readline())

for _ in range(tests):
    length = int(sys.stdin.readline())

    if length == 1:
        print(10)
        exit()

    # 길이가 2인 경우 [길이 1, 길이 2] 이렇게 총 2개의 배열을 만든다
    accumulated_count = [[1] * 10 for _ in range(length)]

    # 길이가 1인 경우 각 숫자로 끝나는 경우의 수는 모두 1개이다 [0으로 끝나는 경우의 수, 1로 끝나는 경우의 수, 2로 끝나는 경우의 수 ...]
    # accumulated_count[0] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    # 길이가 2인 경우 각 숫자로 끝나는 경우의 수를 저장한다 [0으로 끝나는 경우의 수, 1로 끝나는 경우의 수, 2로 끝나는 경우의 수 ...]
    accumulated_count[1] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for i in range(2, length):
        # 모든 길이마다 0으로 끝나는 경우의 수는 항상 1개이므로 건너뛴다
        for j in range(1, 10):
            # j와 같거나 작은 숫자로 끝난 수는 j로 끝나는 줄어들지 않는 숫자를 만들 수 있다
            accumulated_count[i][j] = sum(accumulated_count[i - 1][:j + 1])

    print(sum(accumulated_count[-1]))

