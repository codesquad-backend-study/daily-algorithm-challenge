def solution(sizes):
    w = sizes[0][0]
    h = sizes[0][1]
    area = w * h
    for size in sizes[1:]:
        a = max(w, size[0]) * max(h, size[1])
        b = max(w, size[1]) * max(h, size[0])
        if a < b:
            w = max(w, size[0])
            h = max(h, size[1])
            area = a
        else:
            w = max(w, size[1])
            h = max(h, size[0])
            area = b
    return area


solution([[60, 50], [30, 70], [60, 30], [80, 40]])
