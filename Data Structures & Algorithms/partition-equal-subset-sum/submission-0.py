class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        total = sum(nums)
        if total % 2 !=0:
            return False
        T = total // 2 
        def OPT(j, T):
            if j == 0 and T > 0: 
                return False
            if T == 0:
                return True

            if (j,T) in memo:
                return memo[(j,T)]
            
            if nums[j-1] > T:
                result = OPT(j-1,T)
            else:
                result = OPT(j-1,T-nums[j-1]) or OPT(j-1,T)

            memo[(j,T)] = result
            return result
        
        return OPT(len(nums),T)