class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 두 문자열의 길이를 저장
        m, n = len(text1), len(text2)
        
        # (m+1) x (n+1) 크기의 표를 0으로 초기화
        # +1 하는 이유: 0행/0열을 "빈 문자열" 기저 케이스로 쓰기 위해
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # text1의 각 문자를 순서대로 (i: 1 ~ m)
        for i in range(1, m + 1):
            
            # text2의 각 문자를 순서대로 (j: 1 ~ n)
            for j in range(1, n + 1):
                
                # text1의 i번째 문자 = text1[i-1] (배열은 0부터 시작하므로)
                # text2의 j번째 문자 = text2[j-1]
                if text1[i - 1] == text2[j - 1]:
                    
                    # 문자가 같으면: 공통 수열에 추가 → 대각선 + 1
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    
                else:
                    
                    # 문자가 다르면: 둘 중 하나 포기 → 위/왼쪽 중 최대
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # 표의 오른쪽 하단 = 전체 문자열의 LCS 길이
        return dp[m][n]