class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets=[[] for i in range(len(nums)+1)]

        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        
        for num in freq:
            buckets[freq[num]].append(num)
        res=[]
        for i in range(len(buckets)-1,0,-1):
            arr=buckets[i]
            for num in arr:
                res.append(num)
                if len(res)==k:
                    return res