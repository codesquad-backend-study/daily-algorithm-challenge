input = int(input())

cluster = 1
order = 0
while True:
    if (cluster * (cluster + 1)) // 2 < input:
        cluster += 1
        continue
    else:
        order = input - ((cluster * (cluster - 1)) // 2)
        break
if cluster % 2 == 1:
    print(str((cluster + 1 - order)) + '/' + str(order))
else:
    print(str(order) + '/' + str((cluster + 1 - order)))
