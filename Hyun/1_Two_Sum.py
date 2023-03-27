class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for idx, num in enumerate(nums):
            if num in dic:
                dic[num] = [dic[num], idx]
            else:
                dic[num] = idx

        print(dic)

        for num in nums:
            if target // 2 == num and type(dic[num]) is list:
                return [dic[num][0], dic[num][1]]

            if target // 2 != num and target - num in dic:
                return [dic[num], dic[target - num]]

