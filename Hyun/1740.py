n = int(input())

ans = 0
for idx, bit in enumerate(bin(n)[2:][::-1]):
    if bit == '1':
        ans += 3 ** idx

print(ans)

# 10진수 -> 2진수 -> 3진수 취급해서 곱하며 더한다.
