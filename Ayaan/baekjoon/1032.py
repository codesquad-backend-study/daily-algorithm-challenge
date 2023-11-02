files = []
for _ in range(int(input())):
    files.append(input())

pattern = ""
for i in range(len(files[0])):
    std = files[0][i]
    pattern += std
    for j in range(1, len(files)):
        if std != files[j][i]:
            pattern = pattern[:-1]
            pattern += "?"
            break
print(pattern)
