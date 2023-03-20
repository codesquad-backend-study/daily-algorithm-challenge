class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        cnt = 0
        for num in nums:
            if num == 0:
                cnt += 1

        for i in range(cnt):
            nums.remove(0)
            nums.append(0)    