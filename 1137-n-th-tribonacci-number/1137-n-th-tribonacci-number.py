class Solution:
    def tribonacci(self, n: int) -> int:

        if n == 0:
            return 0
        if n == 1 or n ==2:
            return 1

        dp = [0] * (n+1)
        
        for i in range(3,n+1):

         dp[0] = 0
         dp[1] = 1
         dp[2] = 1

         dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

        return dp[i] 

#T0=0/T1=1/T2=1/T3=T0+T1+T2=1=0+1+1=2 => n
#T4=T1+T2+T3=1+1+2=4/T5=T2+T3+T4=1+2+4=7
