class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        d = [0] * (len(nums) + 1)
        d[0] = 0
        d[1] = nums[0]
        for i in range(2,len(nums)+1):
            d[i] = max((nums[i-1] + d[i-2]), d[i-1])
        return d[len(nums)]
        