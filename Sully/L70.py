# 매번 1계단, 2계단 올라갈 수 있음
# 정상까지 올라갈 수 있는 방법은 몇 가지인지 구하자!
class Solution:
    # DP 방식
    # 시간 복잡도: O(N)
    # Runtime: 31ms
    # Beats: 66.32%
    def climbStairs(self, n: int) -> int:
        # 실제로 n을 1, 2, 3, 4, 5 쭉 적고 하나씩 경우의 수를 세보자
        # 1: 1, 2: 2, 3: 3(2 + 1), 4: 5(2 + 3), 5: 8(3 + 5)
        # 그럼 위와 같이 무언가의 규칙이 생김 -> 이를 아래와 같이 dp의 "점화식"으로 표현할 수 있음
        # f(n) = f(n - 1) + f(n - 2)

        # 첫번째 계단의 경우의 수와 두번째 계단의 경우의 수를 딕셔너리에 저장 (점화식으로 써줘야 하니 2개)
        f = dict()
        f[1] = 1
        f[2] = 2

        # 점화식에서 for문은 보통 3부터 시작하고 n까지의 반복문으로 만들어줌
        # 3번째 계단부터 출발하고, 점화식이 n - 2부터 n까지니까
        for i in range(3, n + 1):
            f[i] = f[i - 1] + f[i - 2]

        return f[n]

    # Memorization 방식 (dp처럼 모든 계단의 수를 다 구할 필요가 사실 없음)
    # 그니까 dp 방식에서는 for문으로 전체의 계단을 다 돈 다음에 결정을 하니까
    # 이 방식에서는 방법 수가 구해지면 그 위에 있는 계단을 계산할 필요가 없는 거지
    # 시간 복잡도: O(N)
    # Runtime: 31ms
    # Beats: 66.32%
    def climbStairs(self, n: int) -> int:
        # n이 1과 2일 때는 아래의 n - 2 값이 음수가 되므로 입력한 n이 그대로 반환되도록 처리
        if n < 3:
            return n

        # 이전과 현재를 각각 첫번째, 두번째 계단의 경우의 수로 저장
        before, current = 1, 2

        # 세번째 계단부터 구하는 로직
        # Memorization을 진행하여 현재와 이전 변수만 계속 저장하여 돌려주는 거지
        # 그래서 n - 2번째까지 돌아주는 거고
        for _ in range(n - 2):
            # 이렇게 한번에 작성하지 않으면 완전 다른 로직임
            # 만약 아래 처럼 작성한다면
            # before = current
            # current = before + current
            # before이 current 변수로 저장이 된 후, current에 또 저장을 하게 되는 거니까
            # 완전히 잘못된 로직으로 바뀜
            before, current = current, before + current

        return current
