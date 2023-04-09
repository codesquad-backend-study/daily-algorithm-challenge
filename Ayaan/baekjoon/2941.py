# O(N)으로 풀기 위해서 1번만 반복하며 조건문으로 풀려고 했는데 실패함...
def solution():
    word = input()
    count = 0
    idx = len(word) - 1
    while(idx >= 0):
        ch = word[idx]
        if ch == "=" or ch == "-" or ch == "j":
            count += 1
            if ch == "j" and idx != 0 and not (word[idx-1] == "l" or word[idx-1] == "n"):
                idx -= 1
            elif ch == "=" and idx - 2 >= 0 and word[idx-2] == "d":
                idx -= 3
            else:
                idx -= 2
        else:
            count += 1
            idx -= 1
    print(count)
    
# replace 이용
def solution2():
    croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
    word = input()
    for val in croatia:
        word = word.replace(val, "c")
    print(len(word))

solution2()