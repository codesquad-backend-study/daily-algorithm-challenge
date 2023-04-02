from typing import List


class Solution:
    # 완전 탐색 방식
    # time: O(N^2)
    # Runtime: 4054 ms -> ㅋㅋㅋㅋㅋㅋ..
    # Beats: 13.63%
    # 이건 버려야겠지?
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []

        # 그냥 말 그대로 모든 경우의 수 비교하면서 더한 값이 target이랑 같은지를 비교하는 거
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # 계속 둘이 더한 값을 비교해주다가 같으면 배열에 저장
                if nums[i] + nums[j] == target:
                    answer = [i, j]

        return answer

    # dict() 방식
    # time: O(N)
    # Runtime: 59ms
    # Beats: 86.75%
    # 자바 Map으로 풀었을 땐 진짜 불편했는데 역시 파이썬
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []

        # 한번 잘 생각해 보자
        # 위 완전 탐색 방식처럼 꼭 두 개를 가지고 비교할 필요가 없고
        # target이 이미 상수값으로 주어져 있으니,
        # target에서 nums의 요소를 빼주면서 비교를 하면 됨
        # 그 차이의 값이 다른 요소에 있으면
        # 비교를 한 자리와 다른 요소의 자리를 리턴하면 됨
        # 중요! 이때의 key와 value는 각각 반대로 생각하자
        # 0, 1, 2, 3의 index가 value에 가도록 반대로 생각
        nums_dict = {}

        # key와 value 한꺼번에 뽑아오는 방법
        # list에서 뽑아오는 거니 key는 그 index가 될 것이고
        for index, value in enumerate(nums):
            # target에서 nums의 요소를 빼주면서 비교
            difference = target - value

            # Only one valid answer exists. < 이 제한이 있으니
            # 같은 index를 가지지 않게 dict 차이점의 value가 key값이랑 같지 않도록
            # 차이가 dict 안에 존재하는지 확인
            if difference in nums_dict:
                # 존재한다면 index인 key를 얻을 수 있으므로 배열에 저장
                # difference key값인 value를 배열에 저장
                answer = [index, nums_dict[difference]]
            else:
                # 존재하지 않는다면 dict 선언할 때 말할 대로
                # index와 value를 반대로 설정해서 계속 추가해주기
                nums_dict[value] = index

        # 이 문제에서 value와 index를 반대로 생각한 이유는
        # dict에서 key를 가지고 value를 찾는 건 쉽지만,
        # value를 가지고 key를 찾는 건 복잡하기 때문
        return answer
