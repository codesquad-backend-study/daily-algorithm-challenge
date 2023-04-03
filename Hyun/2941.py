import re

s = input()
words = re.findall(r'dz=|c=|c-|d-|lj|nj|s=|z=|[a-z]', s)    # 뒤로 갈수록 매칭에서 후순위
print(len(words))

