while True:
    n = list(input())

    if n == ['0']:
        break

    if n[:len(n) // 2] == n[::-1][:len(n) // 2]:        # n[::-1] -> n 을 뒤집는다.
        print("yes")                                    # n[::-1][:len(n) // 2] -> 뒤집은 배열의 0부터 (길이/2 - 1) 인덱스까지의 subList를 만든다.
    else:
        print("no")
