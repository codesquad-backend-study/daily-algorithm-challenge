def solution(arr):
    answer = [arr[0]]
    for each in arr:
        if each != answer[-1]:
            answer.append(each)

    return answer
