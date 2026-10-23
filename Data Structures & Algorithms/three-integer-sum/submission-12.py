class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result_list = []
        sorted_list = sorted(nums)
        for i in range(len(sorted_list)-2):
            j = i + 1
            k = len(sorted_list) - 1
            if i == 0 or sorted_list[i] != sorted_list[i-1]:
                while(j < k):
                    target = -(sorted_list[i])
                    if sorted_list[j] + sorted_list[k] == target:
                        result_list.append([sorted_list[i],sorted_list[j],sorted_list[k]])
                        j = j + 1
                        k = k - 1
                        while j < len(sorted_list) and sorted_list[j] == sorted_list[j-1]:
                            j = j + 1 
                        while k > 0 and sorted_list[k] == sorted_list[k+1]:
                            k = k - 1
                    elif sorted_list[j] + sorted_list[k] > target:
                        k = k - 1
                    else:
                        j = j + 1
        return result_list
                
                
                    
                

    
    