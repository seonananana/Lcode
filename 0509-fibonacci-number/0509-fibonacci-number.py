# F(0)=0, F(1)=1//F(2) = F(1) + F(0) = 1//F(3) = F(2) + F(1) =2
class Solution:
    def fib(self, n: int) -> int:
        
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        dp = [0] * (n+1)

        dp[0] = 0
        dp[1] = 1

        for i in range (2, n+1):
            
            dp[i] = dp[i-1] + dp[i-2]

        
        return dp[n]


