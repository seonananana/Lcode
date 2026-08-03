# 짝수번째 인덱스 값만 모두 더하면 되는거 아닌가? -> 예시는 충족함 하지만 예를들어 [1,2,3,6] 같은 경우는 1+6이 최적 -> dp군
# dp[] -> 점화식: 짝수 인덱스  & 과거 더한 값보다 큰 현재 값
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [0] * n

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[-1]