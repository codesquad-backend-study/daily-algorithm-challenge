import sys

customInput = sys.stdin.readline

cnt1, cnt2 = map(int, customInput().rstrip().split())
db = {}
answer = []
for _ in range(cnt1):
    read = customInput().rstrip()
    db[read] = True
for _ in range(cnt2):
    question = customInput().rstrip()
    if question in db:
        answer.append(question)
answer.sort()
print(len(answer))
print("\n".join(answer))
