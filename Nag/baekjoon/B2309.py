import sys

customInput = sys.stdin.readline

def findAnswer(candidate):
    total = sum(candidate)
    for pointer1 in range(8):
        for pointer2 in range(pointer1 + 1, 9):
            if total - candidate[pointer1] - candidate[pointer2] == 100:
                del candidate[pointer2]
                del candidate[pointer1]
                candidate.sort()
                return


candidate = []
for _ in range(9):
    temp = int(customInput().rstrip())
    candidate.append(temp)
findAnswer(candidate)
print("\n".join(map(str, candidate)))
