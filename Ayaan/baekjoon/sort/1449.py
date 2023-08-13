N, tape = map(int, input().split())
leaks = list(map(int, input().split()))

leaks.sort()
answer = 1
start = leaks[0]
for leak in leaks[1:]:
    # start 부터 테이프 길이에 포함되는 경우 테이프를 더 안써도 됨
    if leak <= start + (tape - 1):
        continue
    # 테이프 길이를 넘어가면 테이프 하나 더 쓰고 start를 다시 설정
    else:
        answer += 1
        start = leak
print(answer)
