class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def OPT(i):
            if i == 0:
                return 0
            if i == 1:
                return nums[i-1]
            if i in memo:
                return memo[i]
            result = max((nums[i-1]+ OPT(i-2)),OPT(i-1))
            memo[i] = result
            return result
        return OPT(len(nums))
        