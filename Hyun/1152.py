s = input()

cnt = 0
if s[0] == ' ':
    s = s[1:]
if len(s) > 0 and s[-1] == ' ':
    s = s[:-1]

print(s.count(' ') + 1 if len(s) > 0 else 0)
