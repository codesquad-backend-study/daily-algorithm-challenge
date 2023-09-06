N = int(input())
budgets = list(map(int, input().split()))
total_budget = int(input())
budgets.sort()

if sum(budgets) <= total_budget:
    print(budgets[-1])
    exit()

answer = 0
# start가 왜 0부터 해야되는지 아시는분?
start = 0
end = budgets[-1]
while start <= end:
    mid = (start + end) // 2
    sum_budget = 0
    for budget in budgets:
        if budget > mid:
            sum_budget += mid
        else:
            sum_budget += budget

    if sum_budget <= total_budget:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)
