class Solution:
    # 0인 것과, 0이 아닌 것 나눠서 생각
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        array_zero = []
        array = []

        for num in nums:
            # 0인 배열 재생성
            if num == 0:
                array_zero.append(num)
            # 0이 아닌 일반 배열 재생성
            else:
                array.append(num)

            # 아래처럼 쓸 수도 있음 (3항)
            # array_zero.append(num) if num == 0 else array.append(num)

        # return 하는 게 아니라 nums에 다시 넣어줘야 함
        # 배열[:]은 전체 슬라이스를 의미 -> 배열의 모든 요소를 선택하는 것과 같음
        # 이렇게 하면 가리키는 객체가 변경되지 않고 해당 객체의 내용만 변경됩 -> 제자리 수정
        nums[:] = array + array_zero