def solution():
    T = int((input()))
    for _ in range(T):
        input_data = input().split()
        n = int(input_data[0])
        result = ""
        for s in input_data[1]:
            result += s * n
        print(result)

solution()
