def solution(routes):
    routes.sort()
    end = 30001
    camera_count = 1

    for route in routes:
        if end < route[0]:
            camera_count += 1
            end = route[1]

        end = min(end, route[1])

    return camera_count
