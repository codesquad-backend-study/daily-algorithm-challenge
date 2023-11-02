n = int(input())
distance = list(map(int, input().split()))
gas_price = list(map(int, input().split()))

current_gas = 1000000001
cost = 0

for idx, gas in enumerate(gas_price[:-1]):
    if gas < current_gas:
        current_gas = gas

    cost += current_gas * distance[idx]

print(cost)
