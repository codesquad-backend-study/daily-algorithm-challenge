for _ in range(int(input())):
    N = int(input())
    heights = list(map(int, input().split()))
    heights.sort(reverse=True)

    nan_e_do = 0
    for i in range(len(heights) - 2):
        nan_e_do = max(nan_e_do, heights[i] - heights[i + 1])
        nan_e_do = max(nan_e_do, heights[i] - heights[i + 2])
    print(nan_e_do)
