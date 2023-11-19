def solution(number, k):
    ans = [number[0]]
    deleted_count = 0

    for num in number[1:]:
        while ans and deleted_count < k and ans[-1] < num:
            ans.pop()
            deleted_count += 1

        ans.append(num)

    while len(ans) > len(number) - k:
        ans.pop()

    return "".join(ans)
