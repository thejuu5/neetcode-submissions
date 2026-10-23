class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
         i = 0 
         j = len(numbers) - 1
         output = []
         while(i!=j):
            if numbers[i] + numbers[j] == target:
                output += [i+1]
                output += [j+1]
                break
            elif numbers[i] + numbers[j] < target:
                i = i + 1
            else:
                j = j - 1
         return output
            
            
            

        