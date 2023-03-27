class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            if not num in dic:
                dic[num] = 1
                continue
            dic[num] += 1
        for key in dic:
            if dic[key] == 1:
                return key
