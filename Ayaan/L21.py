def mergeTwoLists(list1, list2):
    # 밑에서 걸리기 때문에 둘 다 None인 경우 생략 가능
    # if not list1 and not list2:
    #     return list1
    if not list1:
        return list2
    if not list2:
        return list1

    std = list1
    target = list2
    if list2.val < list1.val:
        std = list2
        target = list1
    result = std
    
    while std and target:
        while std.next.val < target.val:
            std = std.next
        std.next, target = target, std.next
        std = std.next
    
    return result
            
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
node1_1 = ListNode(1)
node1_2 = ListNode(2)
node1_3 = ListNode(4)
node2_1 = ListNode(1)
node2_2 = ListNode(3)
node2_3 = ListNode(4)
node1_1.next = node1_2
node1_2.next = node1_3
node2_1.next = node2_2
node2_2.next = node2_3

result = mergeTwoLists(node1_1, node2_1)
print(result)

