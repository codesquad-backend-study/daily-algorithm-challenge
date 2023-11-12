def solution(brown, yellow):
    for h in range(1, brown // 2 + 1):
        for w in range(h, brown):
            if w + w + h + h - 4 == brown:
                if (w - 2) * (h - 2) == yellow:
                    return [w, h]
