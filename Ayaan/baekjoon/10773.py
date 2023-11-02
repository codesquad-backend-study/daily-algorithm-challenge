def solution():
    number_list = []
    for _ in range(int(input())):
        num = int(input())
        if num == 0:
            number_list.pop()
        else:
            number_list.append(num)
    print(sum(number_list))
    
solution()