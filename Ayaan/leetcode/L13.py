def romanToInt(s):
    s = list(s)
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    integer = 0
    for i in range(len(s)):
        # index가 s 길이 넘어간 경우
        if i == len(s):
            break
        cur = s[i]
        
        # index가 마지막인 경우 next 안구함
        if i == len(s)-1:
            integer += roman[cur]
            break
        next = s[i+1]
        
        # next가 더 큰 숫자인 경우
        if roman[cur] < roman[next]:
            integer += roman[next] - roman[cur]
            s.pop(i+1)
        else:
            integer += roman[cur]
    return integer

s = "IX"
print(romanToInt(s))