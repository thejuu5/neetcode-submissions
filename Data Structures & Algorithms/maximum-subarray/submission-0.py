class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memo = {}
        def OPT(i):
            if(i == 0):
                return nums[i]
            if i in memo:
                return memo[i]
            result = max(nums[i],nums[i] + OPT(i-1))
            memo[i] = result
            return result
        return max(OPT(i) for i in range(len(nums)))
        