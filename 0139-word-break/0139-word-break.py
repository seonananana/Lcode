# len(s) > len(word)
# 문자열 s안에 word가 있으면 true, 없으면 False -> case 3 충족 x
# case3 -> dfs or dp
class Solution: 
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
       
       # wordset = set(wordDict)

        n = len(s)

        dp = [False] * (n+1)
        dp[0] = True

        for i in range(1, n+1):

            for j in range(i):

                if dp[j] and s[j:i] in wordDict:

                    dp[i] = True
                
        return dp[n]


