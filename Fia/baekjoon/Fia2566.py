# 시간 제한 1초
# 연산 수 : 9

def find_max_value():
    max_value = 0
    row = 1  # 전부 0일 경우를 생각하여 기본 값을 1로 설정
    column = 1  # 전부 0일 경우를 생각하여 기본 값을 1로 설정

    for i in range(1, 10):
        current_row = list(map(int, input().split()))
        max_in_row = max(current_row)

        if max_in_row > max_value:
            max_value = max_in_row
            row = i
            column = current_row.index(max_in_row) + 1

    print(max_value)
    print(row, column)
