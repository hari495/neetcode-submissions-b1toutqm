class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr=set(nums)
        length=0
        for num in nums:
            if num-1 not in arr:
                l=1
                while num+1 in arr:
                    l+=1
                    num+=1
                length=max(length,l)
        return length
