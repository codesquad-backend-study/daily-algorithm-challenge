from typing import List


class Solution:
    # O(N)으로 풀자!
    def majorityElement(self, nums: List[int]) -> int:
        # O(nlog(n)) 방식
        answer = 0

        # nums of size n
        n = len(nums)
        # 오름차순 정렬 후 절반 나눠가지고 한번 생각해 보자
        nums.sort()
        # n / 2번째에 있는 원소를 리턴??
        answer = nums[n // 2]

        return answer
