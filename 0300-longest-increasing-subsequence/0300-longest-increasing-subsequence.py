class Solution:
    def lengthOfLIS(self, nums):

        # 배열 길이
        n = len(nums)

        # 모든 원소는 자기 자신만 선택해도 길이가 1
        dp = [1] * n

        # 최종 답
        answer = 1

        # i번째 숫자를 하나씩 확인
        for i in range(n):

            # i보다 앞에 있는 모든 숫자를 확인
            for j in range(i):

                # 증가하는 경우
                if nums[j] < nums[i]:

                    # 더 긴 수열을 만들 수 있으면 갱신
                    dp[i] = max(dp[i], dp[j] + 1)

            # 현재까지 가장 긴 길이 저장
            answer = max(answer, dp[i])

        return answer