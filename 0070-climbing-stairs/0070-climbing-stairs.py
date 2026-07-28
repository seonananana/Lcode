class Solution:
    def climbStairs(self, n: int) -> int:

        # 계단이 1개 또는 2개인 경우는
        # 이미 답을 알고 있으므로 바로 반환
        if n <= 2:
            return n

        # first = 1번째 계단까지 가는 방법의 수(dp[1])
        first = 1

        # second = 2번째 계단까지 가는 방법의 수(dp[2])
        second = 2

        # 3번째 계단부터 n번째 계단까지 계산
        for _ in range(3, n + 1):

            # 새로운 값(dp[i])은
            # 이전 두 값(dp[i-1], dp[i-2])의 합이다.
            #
            # 파이썬은 오른쪽을 먼저 계산한 후
            # 왼쪽 변수에 동시에 저장한다.
            #
            # 예)
            # first=1 second=2
            #
            # first, second = second, first+second
            #
            # =>
            # first=2
            # second=3
            first, second = second, first + second

        # 마지막 second가 dp[n]
        return second