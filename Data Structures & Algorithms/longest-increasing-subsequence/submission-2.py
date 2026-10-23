class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def OPT(i, prev):
            if (i,prev) in memo:
                return memo[(i,prev)]
            if i == len(nums):
                return 0
            if(nums[i] <= prev):
                result = OPT(i+1,prev)
            else:
                result = max(1 + OPT(i+1, nums[i]), OPT(i+1,prev)) 
            memo[(i,prev)] = result
            return result
        return OPT(0,float('-inf'))
            
        