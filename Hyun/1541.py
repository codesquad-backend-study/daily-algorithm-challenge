formula = input().split("-")
ans = sum(map(int, formula[0].split("+")))

for each in formula[1:]:
    ans -= sum(map(int, each.split("+")))

print(ans)
