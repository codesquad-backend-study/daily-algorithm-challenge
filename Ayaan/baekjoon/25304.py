def solution():
    total = int(input())
    cal = 0
    for _ in range(int(input())):
        price, amount = map(int, input().split())
        cal += price * amount
    if total == cal:
        print("Yes")
    else:
        print("No")