class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # 방법1. Wrong Answer
        # vs코드에서는 정답 제대로 출력되는데 리트코드에서는 [0,1,0,3,12] -> [0,1,0,3,12,0,0]으로 나옴

        # zero = nums.count(0)
        # nums = [i for i in nums if i != 0]

        # for i in range(zero):
        #     nums.append(0)
        #-----------------------------------------------
        # 방법 2. Accepted
        zeroCount = nums.count(0)
        while 0 not in nums:
            nums.remove(0)
        for i in range(zeroCount):
            nums.append(0)