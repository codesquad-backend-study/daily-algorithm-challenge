from collections import deque

UMM = int(input())


# 이제부터 백준이라도 메서드 분리해주자
def solution():
    N, M = map(int, input().split())
    q_list = list(map(int, input().split()))
    q = deque(q_list)
    case = 0
    # 0에서 1을 뺀 게 -1이니까 그전까지 계속 돌아줘
    while M != -1:
        # 큐에서 가장 큰 값이 첫번째 값이랑 같으면
        if max(q) == q[0]:
            # 첫번째를 꺼내줌
            q.popleft()
            # 첫번째 (하나) 꺼내줬으니 다시 채워줘야지 그치?
            case += 1
            # M 앞으로 한칸 이동
            M -= 1
            # else 쓰기 싫어서 껀띠뉴 사용
            continue

        # 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면,
        # 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. (문제 조건이야)
        q.append(q.popleft())

        if M == 0:
            # M도 같이 맨뒤자리로 이동하는 거야 (위에서 append, popleft 해줬짢아)
            M = len(q) - 1
        else:
            # 앞으로 한칸
            M -= 1

    return case


# 돌리기
for _ in range(UMM):
    print(solution())
