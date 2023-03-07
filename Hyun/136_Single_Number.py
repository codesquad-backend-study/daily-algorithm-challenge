import collections


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)

        return counter.most_common()[-1][0]