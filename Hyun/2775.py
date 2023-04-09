t = int(input())

for _ in range(t):
    floor = int(input())
    room_number = int(input())

    people = [[0] * (room_number + 1) for _ in range(floor + 1)]    # 사람수를 나타내느 2차원 배열

    for r in range(1, room_number + 1):
        people[0][r] = r                                            # 0층의 사람수 세팅

    for f in range(1, floor + 1):                                   # f 층의 r 호의 사람수를 구하는 이중 for 문
        for r in range(1, room_number + 1):
            people[f][r] = sum(people[f - 1][:r + 1])               # people[f - 1] -> 아랫층 전체
                                                                    # people[f - 1][:r + 1] -> 아랫층 전체에서 1호부터 r호 까지만 배열만 슬라이싱
    print(people[floor][room_number])                               # sum(people[f - 1][:r + 1]) -> 그것의 합 
