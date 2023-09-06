import sys


def solution():
    M = int(sys.stdin.readline().rstrip())
    S = set()

    for _ in range(M):
        tmp_input = sys.stdin.readline().rstrip()

        if tmp_input == "all" or tmp_input == "empty":
            command = tmp_input
        else:
            command, tmp_str_num = tmp_input.split()
            x = int(tmp_str_num)

        if command == "add" and x not in S:
            S.add(x)

        elif command == "remove" and x in S:
            S.remove(x)

        elif command == "check":
            if x in S:
                print(1)
                continue

            print(0)

        elif command == "toggle":
            if x in S:
                S.remove(x)
                continue

            S.add(x)

        elif command == "all":
            S = {i for i in range(1, 21)}

        elif command == "empty":
            S = set()


solution()
