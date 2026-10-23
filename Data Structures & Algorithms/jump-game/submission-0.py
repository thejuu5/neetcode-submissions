class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}
        def OPT(i):
            if i in memo:
                return memo[i]
            if i == len(nums) - 1:
                return True
            result = False
            for j in range (i+1, min(nums[i]+i,len(nums)-1) + 1):
               if OPT(j):
                  result = True
                  break
            memo[i] = result
            return result
        return OPT(0)

        