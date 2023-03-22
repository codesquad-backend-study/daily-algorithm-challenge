def isPalindrome(head):
    if head.next is None:
        return True
        
    numList = head
    while head:
        numList.append(head.val)
        head = head.next
    
    mid = len(numList) // 2
    # right는 오른쪽 리스트의 시작지점인데
    # numList의 길이가 홀수이면 1 커야한다.
    if len(numList) % 2 == 0:
        right = mid - 1
    else:
        right = mid
    # (0~mid-1) == (끝 ~ right+1) 절반을 나눠서 같은지 비교한다.
    if numList[0:mid] == numList[-1:right:-1]:
        return True
