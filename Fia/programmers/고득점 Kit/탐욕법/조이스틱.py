def solution(name):
    slide = 0
    min_move = len(name) - 1

    for i, char in enumerate(name):
        slide += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        min_move = min([min_move, 2 * i + len(name) - next, 2 * (len(name) - next) + i])

    return slide + min_move
