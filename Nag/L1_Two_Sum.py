class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       answer = []
       for i in range(0, len(nums)):
           for j in range(i + 1, len(nums)):
               if(nums[i] + nums[j] == target):
                   answer.append(i)
                   answer.append(j)
                   return answer
        # 맨처음 코드, 2중 반복문 돌렸습니다. 직관적인 풀이지만 개쓰래기 코드입니다

    #궁금해서 찾아본 코드 dictionary(자바에서는 map)사용
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic = {}
        # enumerate 핵좋은듯, 인덱스와 요소를 동시에 반복문으로 돌릴 수 있습니다
        # dic에다가는 element와 index를 저장, 중요한 점은 반복문 돌리면서 index를 계속 저장한다는 점
        # 그래서 반복문이 진행될수록 diff가 dic에 있는지 확인하고 있으면 dic에 저장된 index와 지금의 index를 반환
        for index, element in enumerate(nums):
            diff = target - element
            if diff in dic:
                return [dic[diff], index]
            dic[element] = index
