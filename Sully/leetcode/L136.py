from typing import List


class Solution:
    # 비어 있지 않은 정수 배열이 주어졌을 때, 한 개를 제외한 모든 요소가 두 번 나타남
    # 그 제외된 한 개의 요소가 무엇인지 찾자!
    # linear runtime complexity: O(N) 시간 복잡도
    def singleNumber(self, nums: List[int]) -> int:
        # 쓰레기
        # nums.sort()
        # # 정렬하면 답은 nums[len(nums) - 1] or nums[0]
        # if len(nums) > 1:
        #     if nums[0] == nums[1]:
        #         return nums[len(nums) - 1]
        #     if nums[len(nums) - 1] == nums[len(nums) - 2]:
        #         return nums[0]
        # else:  # Example 3과 같은 상황
        #     return nums[0]

        # i-1과 i를 계속 돌면서 cnt를 증가시켜볼까..? -> X
        # 위처럼 쓰지 말고 XOR 비트 연산자 사용하자
        # 2개가 같을 때 체크되는 아이디어로!
        answer = 0
        for i in nums:
            answer ^= i

        return answer

print(Solution().singleNumber([2, 2, 1]))
print(Solution().singleNumber([4, 1, 2, 1, 2]))
print(Solution().singleNumber([1]))

# Expected: 354
print(Solution().singleNumber(
    [-336, 513, -560, -481, -174, 101, -997, 40, -527, -784, -283, -336, 513, -560, -481, -174, 101, -997, 40, -527,
     -784, -283, 354]))
