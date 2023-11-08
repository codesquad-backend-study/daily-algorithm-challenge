def solution(brown, yellow):
    i = 1
    while i <= (yellow // i):
        if yellow % i == 0:
            yellow_x = yellow // i
            yellow_y = i

            width = yellow_x + 2
            height = yellow_y + 2
            if width * height == brown + yellow:
                return [width, height]
        i += 1
