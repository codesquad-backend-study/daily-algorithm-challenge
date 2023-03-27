# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # list1의 끝 노드를 알아야 됨 (null일 때까지 이동해야 되니)
    # 처음은 포인터가 각각 처음을 가리키게 함
    # 작은 값을 담고 있는 노드를 추가하고, 포인터를 다음 노드로 전지닛킴
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy: LinkedList에서 자주 사용됨 (경계 조건을 처리하는 데 훨씬 수월해짐)
        dummy = ListNode()
        end = dummy

        # Example 2, 3 처리
        if list1 is None:
            return list2

        if list2 is None:
            return list1

        # 둘 다 null이 아닐 때
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                end.next = list1  # list1이 병합된 다음 노드
                list1 = list1.next  # 다음 노드로 포인터 이동
            else:  # list.val >= list2.val
                end.next = list2  # list2이 병합된 다음 노드
                list2 = list2.next  # 다음 노드로 포인터 이동

            # 업데이트를 해줘야 병합된 것도 이동해주지
            end = end.next

        # while문을 빠져나왔다는 것은 list1, list2 둘 중 하나가 null이라는 것
        # null이 아닌 쪽에 있는 list의 남은 노드를 병합된 것에 추가
        end.next = list1 or list2
        # 아래 코드를 위의 코드처럼 줄여 쓸 수 있음
        # if list1:
        #     end.next = list1
        # elif list2:
        #     end.next = list2

        return dummy.next
