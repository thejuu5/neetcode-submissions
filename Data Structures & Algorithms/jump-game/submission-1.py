class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[len(nums)-1] = True
        for i in range (len(nums)-2,-1,-1):
            for j in range (i+1, min(nums[i]+i,len(nums)-1) + 1):
                dp[i] = dp[i] or dp[j] 
        return dp[0]
        