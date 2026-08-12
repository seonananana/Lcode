# 0부터 시작하면 안됨 
# 12 -> 1,2 / 12 ->2
# 123 -> 1,2,3/ 1,23 , 12, 3/ 123 ->3
# 1234 -> 1,2,3,4/ 1,23,4/ 1,2,34 / 12, 34/ 1, 234, 123, 4/ ->5
# dp 구나. 앞의 규칙을 그대로 가져옴
# case 3 불충족..숫자가
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        # dp[i] = s의 앞에서 i개를 해석하는 방법의 수
        dp = [0] * (n + 1)

        # 아무것도 해석하지 않은 경우
        dp[0] = 1

        # 첫 번째 문자가 0이면 해석 불가능
        if s[0] == '0':
            return 0

        # 한 글자는 1~9이므로 하나의 방법
        dp[1] = 1

        for i in range(2, n + 1):

            # 한 자리 숫자로 해석
            one = int(s[i - 1])

            if 1 <= one <= 9:
                dp[i] += dp[i - 1]

            # 두 자리 숫자로 해석
            two = int(s[i - 2:i])

            if 10 <= two <= 26:
                dp[i] += dp[i - 2]

        return dp[n]