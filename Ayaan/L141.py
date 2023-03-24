def hasCycle(self, head: Optional[ListNode]) -> bool:
    nodeCountList = {}
    
    while head and head.next:
        # 노드들의 개수를 딕셔너리에 저장한다.
        if head in nodeCountList:
            nodeCountList[head] += 1
        else:
            nodeCountList[head] = 1
        
        # 개수가 2개가 되면 사이클이 되니 True
        if nodeCountList[head] == 2:
            return True

        head = head.next

    return False

def hasCycle(self, head: Optional[ListNode]) -> bool:
    slow = head
    fast = head
    # 한칸씩 앞으로 가는 slow와 두칸씩 앞으로 가는 fast
    # 사이클인 경우 slow와 fast가 언젠간 같아지는 순간이 온다.
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        
        if fast == slow:
            return True

    return False