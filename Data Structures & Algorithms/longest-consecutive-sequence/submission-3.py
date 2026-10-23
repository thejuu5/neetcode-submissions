class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        sorted_set = set(nums)
        nums1 = sorted(list(sorted_set))
        flag = 0
        count = 0
        for i in range(0,len(nums1)-1):
            if (nums1[i+1] - nums1[i]) == 1:
                count = count+1
                if count > flag:
                    flag = count
            else:
                count = 0
        
        return flag+1