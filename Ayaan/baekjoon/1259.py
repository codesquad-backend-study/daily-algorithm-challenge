while(True):
    num = input()
    if num == "0":
        break
    
    mid = len(num) // 2
    if len(num) % 2 != 0:
        mid += 1
    
    if num[0:len(num)//2] == num[mid:][::-1]:
        print("yes")
    else:
        print("no")    
