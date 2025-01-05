class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # if len(s1)+len(s2)<len(s3):
        #     return False
        dp = [[-1 for _ in range(len(s2)+1)]for _ in range(len(s1)+1)]
        def helper(i1, i2, i3):
            if i3==len(s3):
                if i1==len(s1) and i2==len(s2):
                    return True
                return False
            if i1<len(s1) and i2<len(s2):
                if dp[i1][i2]!=-1:
                    return dp[i1][i2]
            if i1<len(s1) and s1[i1]==s3[i3]:
                if helper(i1+1,i2,i3+1):
                    dp[i1][i2] = True
                    return dp[i1][i2]
            if i2<len(s2) and s2[i2]==s3[i3]:
                if helper(i1,i2+1,i3+1):
                    dp[i1][i2] = True
                    return dp[i1][i2]
                
            dp[i1][i2] = False
            return dp[i1][i2]
            

        return helper(0,0,0)
        