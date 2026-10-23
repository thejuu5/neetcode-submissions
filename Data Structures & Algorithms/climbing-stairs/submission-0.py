class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def OPT(i):
            if i == 0:
                return 1
            if i == 1:
                return 1
            if i in memo:
                return memo[i]
            result = OPT(i-1) + OPT(i-2)
            memo[i] = result
            return result
        return OPT(n)
        
        