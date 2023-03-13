from typing import List


class Solution:
    # 그냥 단순하게 바로 전 행의 (현재와 바로 전의 열)을 추가해나가면 됨
    def generate(self, numRows: int) -> List[List[int]]:
        # 항상 첫 번째 행은 1
        pascal = [[1]]

        # 그 다음 행까지 비교하는 거니까 1을 안 빼주면 범위 에러
        for i in range(numRows - 1):
            # tmp 행 저장하고 계속 초기화시킴 (똑같이 항상 첫 번째 행은 1)
            tmp = [1]  # 처음의 1

            # j가 0에서 i까지의 범위에 있을 때까지(정삼각형) 아래를 반복
            for j in range(0, i):
                # i 행의 j번째 요소와 j+1번째 요소를 더한다는 것은
                # 위에서 설명한 것처럼 바로 전 행의 (현재와, 바로 전의 열)을 추가하는 것과 똑같은 소리 (뒤집어서)
                tmp.append(pascal[i][j] + pascal[i][j + 1])

            # 마지막의 1
            tmp.append(1)
            # 한줄이 완성됐으니 이걸 계속 추가해나가면 삼각형 완성
            pascal.append(tmp)

        return pascal


print(Solution().generate(5))
print(Solution().generate(1))
