class Solution:
    def rob_one(self, nums: List[int]) -> int:
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
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        split_excluding_last = self.rob_one(nums[:-1])
        split_excluding_first = self.rob_one(nums[1:])
        return max(split_excluding_last, split_excluding_first)


        