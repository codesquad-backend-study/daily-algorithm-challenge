import collections

S, length = map(int, input().split())
dna = input()
A, C, G, T = map(int, input().split())

answer = 0
count = collections.Counter(dna[:length])
if count['A'] >= A:
    if count['C'] >= C:
        if count['T'] >= T:
            if count['G'] >= G:
                answer += 1

for i in range(1, len(dna) - length + 1):
    count[dna[i - 1]] -= 1
    count[dna[i + length - 1]] += 1
    if count['A'] >= A:
        if count['C'] >= C:
            if count['T'] >= T:
                if count['G'] >= G:
                    answer += 1

print(answer)
