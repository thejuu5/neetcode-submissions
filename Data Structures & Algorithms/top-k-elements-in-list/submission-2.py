class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        list_num = []
        bucket = [[] for i in range(len(nums)+1)]
        dict_num = dict(Counter(nums))
        for key,value in dict_num.items():
            bucket[value].append(key)
        for i in range(len(nums),-1,-1):
            if bucket[i]!= " " and k!=0:
                list_num += bucket[i]
                k=k-len(bucket[i])
        
        return list_num
        