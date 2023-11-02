for _ in range(int(input())):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    B.sort()


    def binary_search(num):
        start = 0
        end = len(B) - 1
        count = 0
        while start <= end:
            mid = (start + end) // 2
            if num <= B[mid]:
                end = mid - 1
            else:
                start = mid + 1
                count = mid + 1
        return count


    answer = 0
    for num in A:
        answer += binary_search(num)

    print(answer)
