class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0] * (len(nums) + 1)
        right = [0] * (len(nums)+1)
        output = [0] * (len(nums))
        for i in range(0,len(nums)):
            if i == 0:
                left[i] = 1
            else:
                left[i] = left[i-1] * nums[i-1]

        for j in range(len(nums)-1,-1,-1):
            if  j == len(nums)-1:
                right[j] = 1
            else:
                right[j] = right[j+1] * nums[j+1]

        for k in range(0,len(nums)):
            output[k] = left[k] * right[k]
        
        return output
        
