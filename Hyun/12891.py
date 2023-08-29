import collections


def check():
    for each in dna:
        if currents[each] < needs[each]:
            return False

    return True


dna = ["A", "C", "G", "T"]

entire_len, sub_len = map(int, input().split())
string = input()
need_cnt = list(map(int, input().split()))

needs = {dna[i]: need_cnt[i] for i in range(4)}
currents = {"A": 0, "C": 0, "G": 0, "T": 0}

queue = collections.deque(string[:sub_len])

for ch in string[:sub_len]:
    if ch in currents:
        currents[ch] += 1

ans = 0
if check():
    ans += 1

for i in range(sub_len, entire_len):
    if string[i] in currents:
        currents[string[i]] += 1
    queue.append(string[i])

    pop = queue.popleft()
    if pop in currents:
        currents[pop] -= 1

    if check():
        ans += 1

print(ans)
