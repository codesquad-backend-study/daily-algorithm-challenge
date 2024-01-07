def solution(n, times):
    answer = 0

    # right는 가장 비효율적으로 심사했을 때 걸리는 시간이다
    # 즉, 가장 긴 심사 시간을 갖는 심사관에서 n명 모두 심사받는 경우이다.
    left = 1
    right = max(times) * n

    while left <= right:
        mid = (left + right) // 2
        people = 0  # 모든 심사관이 mid분 동안 심사한 사람의 수

        for time in times:
            people += mid // time

            # 모든 심사관을 거치지 않아도 mid분 동안 n명 이상 심사할 수 있다면 반복문을 탈출한다
            if people >= n:
                break

        # 심사한 사람의 수가 심사를 받을 사람의 수보다 많거나 같은 경우
        if people >= n:
            answer = mid
            right = mid - 1
        # 심사한 사람의 수가 심사를 받을 사람의 수보다 적은 경우
        elif people < n:
            left = mid + 1

    return answer
