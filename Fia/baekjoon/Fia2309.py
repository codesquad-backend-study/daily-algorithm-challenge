# 일곱 난쟁이

nine = []
for _ in range(9):
    nine.append(int(input()))

nine.sort()

left = 7
right = 8
while True:
    seven = sum(nine) - (nine[left] + nine[right])
    if seven == 100:
        del nine[right]
        del nine[left]
        break
    elif seven < 100:
        left -= 1
        right -= 1
    else:
        right += 1

print(*nine, sep='\n')
