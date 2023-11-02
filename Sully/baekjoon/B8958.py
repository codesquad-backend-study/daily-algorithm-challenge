import sys

# 문제의 개수
n = int(sys.stdin.readline())

# 점수 배열 만들기
score_list = []
for i in range(n):
    # 여기서 strip() 안 쓰면 \n 붙음..
    score_list.append(sys.stdin.readline().strip())

# 메인 로직
for score in score_list:
    # 전체 반복문마다 초기화
    tmp_score = 0
    count_O = 0

    # 한줄씩 점수 계속 저장
    for each in score:
        # O가 연속되면 하나씩 계속 추가
        if each == 'O':
            count_O += 1
            tmp_score += count_O
        else:  # each == 'X'
            count_O = 0

    # 결과 한줄씩 출력
    print(tmp_score)
