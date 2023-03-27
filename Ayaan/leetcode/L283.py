class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # n~0까지 반복
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
        return nums