import sys

N, M = map(int, sys.stdin.readline().split())
trains = [0] * (N + 1)
for _ in range(M):
    command = list(map(int, sys.stdin.readline().split()))
    if command[0] == 1:
        trains[command[1]] |= 1 << (20 - command[2])
    elif command[0] == 2:
        trains[command[1]] &= ~(1 << (20 - command[2]))
    elif command[0] == 3:
        trains[command[1]] >>= 1
    else:
        trains[command[1]] <<= 1
        trains[command[1]] &= ~(1 << 20)

print(len(set(trains[1:])))
