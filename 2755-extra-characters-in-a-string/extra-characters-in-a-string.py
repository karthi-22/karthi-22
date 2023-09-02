class Solution:
    def minExtraChar(self, s: str, dic: List[str]) -> int:
        n = len(s)
        dic_set = set(dic)
        dp = [0]*(n+1)
        for i in range(n-1,-1,-1):
            dp[i] = 1+dp[i+1]
            for j in range(i,n):
                curr = s[i:j+1]
                if curr in dic_set:
                    dp[i] = min(dp[i],dp[j+1])
        return dp[0]