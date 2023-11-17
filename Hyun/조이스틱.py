def solution(name):
    slide = 0
    min_move = len(name) - 1  # 그냥 왼쪽에서 오른쪽으로 쭉 가기

    for i, ch in enumerate(name):
        slide += min(ord(ch) - ord('A'), 26 - ((ord(ch)) - ord('A')))

        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        min_move = min(min_move,
                       2 * i + len(name) - next,    # 시작 지점에서 긴 A가 시작되지 않는 지점까지 오른쪽 이동 후 왼쪽으로 계속 이동
                       2 * (len(name) - next) + i)  # 시작 지점에서 긴 A가 시작되지 않는 지점까지 왼쪽으로 이동 후 오른쪽으로 계속 이동

    return slide + min_move

# 참고 블로그: https://velog.io/@jqdjhy/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A1%B0%EC%9D%B4%EC%8A%A4%ED%8B%B1-Greedy
