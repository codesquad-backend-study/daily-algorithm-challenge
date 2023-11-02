def solution(arr):
    answer = []
    prev = arr[0]
    for num in arr[1:]:
        if prev != num:
            answer.append(prev)
            prev = num
    answer.append(prev)
    return answer
