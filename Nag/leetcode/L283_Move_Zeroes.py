class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        cnt = 0
        index = 0
        
        #계속 없애기 위해서 for 말고 while 사용
        while True:
            if index == len(nums):
                break
            if nums[index] == 0:
                cnt += 1
                del nums[index]
            else:
                index += 1
        for i in range(cnt):
            nums.append(0)               
