# 공간복잡도 O(n)
class Solution:
    def majorityElement(nums):
        count_data = {}
        for i in nums:
            if i not in count_data:
                count_data[i] = 0
            count_data[i] += 1
        
        for key, value in count_data.items():
            if value > (len(nums)//2):
                return key
    
    # Solution 코드
    # 공간복잡도 O(1)
    # 정렬하면 항상 n/2번째 숫자가 정답이 된다.
    # 이렇게 푼다면 천재이다.
    def majorityElement2(nums):
        nums.sort()
        return nums[len(nums) // 2]
    
    nums = [3,2,2,3,1,3,2,2,2]
    result = majorityElement2(nums)
    print(result)