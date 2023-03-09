from typing import List


class Solution:
    # O(N)으로 풀자!
    def majorityElement(self, nums: List[int]) -> int:
        # O(n) 방식
        answer = 0
        dict_cnt = dict()
        max_key = 0

        # 배열의 원소가 몇번 나왔나 dict_cnt에 기억을 해줌
        for num in nums:
            if num in dict_cnt:
                # for문 돌다가 또 나왔으면 1 추가
                dict_cnt[num] = dict_cnt[num] + 1
            else:
                dict_cnt[num] = 1

        # dict_cnt 맵 반복
        for key in dict_cnt:
            if dict_cnt[key] > max_key:
                max_key = dict_cnt[key]
                # 가장 많이 나온 key를 answer에 저장
                answer = key

        return answer

        # O(nlog(n)) 방식
        # answer = 0
        #
        # # nums of size n
        # n = len(nums)
        # # 오름차순 정렬 후 절반 나눠가지고 한번 생각해 보자
        # nums.sort()
        # # n / 2번째에 있는 원소를 리턴??
        # answer = nums[n // 2]
        #
        # return answer


print(Solution().majorityElement([3, 2, 3]))
print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))
