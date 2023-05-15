# 시간 제한 2초
# 파일 이름의 개수 N : 0 < N <= 50
# 파일 이름의 길이 L : 0 < L <= 50

# 파일 이름에서 공통되지 않은 부분을 "?"로 변경하면서 전부 확인하는 방법
# 연산 수 : N * L

def find_pattern():
    number_of_file = int(input())
    first_file_name = input()

    if number_of_file == 1:
        print(first_file_name)
        exit()

    common = list(first_file_name)

    for _ in range(1, number_of_file):
        file_name = input()
        for index, char in enumerate(file_name):
            if first_file_name[index] != char:
                common[index] = "?"

    print("".join(common))
