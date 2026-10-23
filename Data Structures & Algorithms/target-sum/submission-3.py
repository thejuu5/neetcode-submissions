class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def OPT(i,j):
            if i == -1 and j == 0:
                return 1
            if i == -1 and j != 0:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            result = OPT(i-1, j - nums[i-1]) + OPT(i-1,j + nums[i-1])
            memo[(i,j)] = result
            return result
        return OPT(len(nums)-1,target)
        