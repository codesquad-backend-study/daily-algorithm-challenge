n = int(input())
budgets = list(map(int, input().split()))
total_budget = int(input())

ans = -1

start = 0
end = max(budgets)
while start <= end:
    mid = (start + end) // 2

    expected_budget = 0
    for budget in budgets:
        expected_budget += min(budget, mid)

    if expected_budget <= total_budget:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1

print(ans)
