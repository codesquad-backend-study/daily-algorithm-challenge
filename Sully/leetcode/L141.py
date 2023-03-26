# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# LinkedList에서 사이클이 존재하면 True 리턴하는 문제
class Solution:
    # Set 방식
    # time: O(N)
    # Runtime: 55ms
    # Beats: 74.8%
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 무한 루프에 걸리지 않도록 주의해서
        # 사이클 부분 판단 후 반복문 빠져나오게 하자
        visit_set = set()

        # head가 null이 아니면 계속 반복문 돌아주기
        while head is not None:
            # head가 visit_set에 이미 존재하면 True 리턴
            # 왜냐면 이미 있다는 것은 그 노드가 이미 방문되었다는 거니까
            if head in visit_set:
                return True

            # set을 계속 넣어줘야지 판단을 하지
            # head가 이동(.next)하면서 계속 set에 기본값을 넣어주는(add) 거야
            visit_set.add(head)
            head = head.next

        # 반복문을 빠져나왔다는 것은 이미 null이라는 것이고
        # True가 안 되었으니 방문한 적도 없었다는 것이니
        # False 리턴
        return False

    # 순환 탐지 알고리즘인
    # Floyd's tortoise and hare 알고리즘 방식
    # 첫번째 포인터는 거북이처럼 느리게 포인터를 이동하고
    # 두번쨰 포인터는 토끼처럼 빠르게 포인터를 이동
    # 그럼 언젠가는 둘이 만나게 됨
    # time: O(N)
    # Runtime: 59ms
    # Beats: 51.97%
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 거북이 포인터, 토끼 포인터 각각 LinkedList의 head를 가리키도록 하자
        turtle_pointer, rabbit_pointer = head, head

        # 토끼를 기준으로 하는 이유는 토끼를 중점으로 생각하는 알고리즘 방식이기 때문 (토끼 먼저 진행)
        # next를 체크하는 이유는 토끼가 2칸을 한꺼번에 이동하기 때문
        while rabbit_pointer is not None and rabbit_pointer.next is not None:
            # 거북이는 1칸
            turtle_pointer = turtle_pointer.next
            # 토끼는 2칸
            rabbit_pointer = rabbit_pointer.next.next

            # 막 달리다가 둘이 만나면 True 리턴
            if turtle_pointer == rabbit_pointer:
                return True

        # 반복문 빠져나오면 둘이 못 만나고 null이 된 거니까 False 리턴
        return False
