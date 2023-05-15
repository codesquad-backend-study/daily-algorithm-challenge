import sys

cnt = int(sys.stdin.readline().rstrip())
answer = []
for _ in range(cnt):
    file = sys.stdin.readline().rstrip()
    if cnt == 1:
        answer = list(file)
        break
    if not answer:
        answer = list(file)
        continue
    for index in range(len(answer)):
        if answer[index] != file[index]:
            answer[index] = "?"
print("".join(answer))
