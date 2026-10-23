class Solution:
    def search(self, nums: List[int], target: int) -> int:
        m = len(nums) // 2
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else: 
                return -1
        if target <= nums[m-1]:
            return self.Search(nums[:m],0,target)

        else:
            return self.Search(nums[m:],m,target)
            


    def Search(self, nums1: List[int], begin_index: int, target: int) -> int:
        end_index = len(nums1) + begin_index
        j = 0 
        for i in range (begin_index, end_index):
            if nums1[j] == target:
                j = j + 1
                return i
                break
            else:
                j = j + 1
        return -1
        