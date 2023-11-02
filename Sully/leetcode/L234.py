# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 시간 복잡도: O(N)
    # Runtime: 754ms
    # Beats: 83.59%
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 처음에 head가 null인 값도 처리를 해줘야 하는 줄 알았었지만
        # 오히려 속도만 늦출 뿐 필요가 없었음
        # Optional로 감싸서 들어오니 당연히 필요가 없지

        array = []
        current = head

        # linkedList의 모든 값을 array 배열에 순차적으로 저장
        # current (head)가 null이 아닐 때 반복문 돌아주자
        while current is not None:
            # 배열에 계속 추가해주고
            array.append(current.val)
            # 노드 오른쪽으로 이동시켜주기
            current = current.next

        # [::-1] -> 배열 뒤집기
        # 그냥 배열과 그 뒤집은 배열이 동일하면 true를 리턴하게끔
        return array == array[::-1]
