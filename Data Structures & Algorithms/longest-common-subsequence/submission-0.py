class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def OPT(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i == len(text1):
                return 0
            if j == len(text2):
                return 0
            if text1[i] == text2[j]:
                result = 1 + OPT(i+1,j+1)
            else:
                result = max(OPT(i,j+1),OPT(i+1,j))
            memo[(i,j)] = result
            return result
        return OPT(0,0)
        