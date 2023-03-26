# 시간복잡도 O(N^2)
# 브루트포스 : 이중 반복문을 사용해 경우의 수를 모두 찾아본다.
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
            
# 시간복잡도 O(N)
# dictionary를 사용해서 값과 index를 넣는다.
# 합이 target이 되는 값이 있는지 확인하기 위해 in을 사용하면 O(1)이 된다.
def twoSum(self, nums: List[int], target: int) -> List[int]:
    numDict = {}

    for i in range(len(nums)):
        if target - nums[i] in numDict:
            return [numDict[target - nums[i]], i]
        numDict[nums[i]] = i