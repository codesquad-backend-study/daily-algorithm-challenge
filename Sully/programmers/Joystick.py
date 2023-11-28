def solution(name: str):
    # 상하 이동
    up_down = 0
    name_length = len(name)
    # 좌우 이동 (한쪽 방향으로 계속 움직였을 경우을 저장, 즉 최댓값을 저장해 둠)
    left_right = name_length - 1

    for i, c in enumerate(name):
        # 상하 이동 최솟값 저장 (알파벳 이동)
        up_down += min(ord(c) - ord('A'), ord('Z') - ord(c) + 1)

        # 다음 index부터의 연속된 A 문자열 찾기 (몇 개인지)
        next_i = i + 1
        while next_i < name_length and name[next_i] == 'A':
            next_i += 1

        # 좌우 이동 최솟값 저장 (커서 이동)
        # ->
        # 이전 이동 값
        # 연속된 A 문자열의 왼쪽 시작
        # 연속된 A 문자열의 오른쪽 시작
        left_right = min([
            # (name_length - next_i): 현재 위치 다음부터 나오는 연속된 A 문자열의 길이
            left_right,
            # i * 2는 현재 내 위치까지 왔다가 (i), 다시 처음 위치로 돌아가는 (i * 2) 의미
            # 오른쪽으로 갔다가 다시 왼쪽으로 꺾기
            (i * 2) + (name_length - next_i),
            # 왼쪽으로 갔다가 다시 오른쪽으로 꺾기
            # i는 현재 위치로 간다는 의미고
            # (name_length - next_i) * 2는 A 문자열을 뛰어넘은 후 다시 문자열 끝에 도달하는 데 필요
            i + (name_length - next_i) * 2
        ])

    # 상하 + 좌우
    return up_down + left_right


print(solution('JEROEN'))
print(solution('JAN'))
