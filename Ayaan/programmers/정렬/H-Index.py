def solution(citations):
    citations.sort(reverse=True)

    for i in range(len(citations)):
        # 내림차순으로 정렬했기 때문에
        # i + 1은 i번째 값보다 크거나 같은 값의 개수
        # i + 1이 i번째 논문의 인용 수보다 크거나 같아지면 i가 H-index
        if i + 1 >= citations[i]:
            return i

    return len(citations)


solution([3, 0, 6, 1, 5])
