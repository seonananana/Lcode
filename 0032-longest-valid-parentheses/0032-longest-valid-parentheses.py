class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)

        # dp[i] = i번째 문자까지 고려했을 때,
        # i번째 문자에서 끝나는 유효한 괄호 문자열의 길이
        dp = [0] * n

        answer = 0

        for i in range(1, n):
            # 현재 문자가 ')'여야 유효한 괄호가 끝날 수 있음
            if s[i] == ')':

                # 바로 앞이 '('인 경우
                # ()
                if s[i - 1] == '(':
                    dp[i] = 2

                    # 그 앞에 유효한 괄호가 있었다면 이어 붙임
                    if i >= 2:
                        dp[i] += dp[i - 2]

                # 현재가 "))" 형태인 경우
                # ...))
                elif s[i - 1] == ')':
                    # 이전에 만들어진 유효한 괄호의 앞쪽 문자를 확인
                    j = i - dp[i - 1] - 1

                    if j >= 0 and s[j] == '(':
                        dp[i] = dp[i - 1] + 2

                        # 더 앞에 유효한 괄호가 있다면 이어 붙임
                        if j >= 1:
                            dp[i] += dp[j - 1]

            answer = max(answer, dp[i])

        return answer