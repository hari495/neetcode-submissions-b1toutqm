class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        length=0
        for num in nums:
            if not num-1 in nums:
                seq_length=1
                while (num+1) in nums:
                    seq_length+=1
                    num+=1
                length=max(length,seq_length)
        return length
