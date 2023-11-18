def solution(routes):
    routes.sort()
    start = -30001
    end = 30001
    camera_count = 1

    for route in routes:
        if end < route[0]:
            camera_count += 1
            start = route[0]
            end = route[1]

        start = max(start, route[0])
        end = min(end, route[1])

    return camera_count
