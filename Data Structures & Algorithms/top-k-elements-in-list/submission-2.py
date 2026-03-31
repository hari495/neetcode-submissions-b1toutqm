class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts=[[] for i in range(len(nums)+1)]
        
        freq={}
        for num in nums:
            freq[num]=1+freq.get(num,0)
        
        for num in freq:
            counts[freq[num]].append(num)
        
        res=[]
        for i in range(len(counts)-1,0,-1):
            arr=counts[i]
            for num in arr:
                res.append(num)
                if (len(res) == k):
                    return res