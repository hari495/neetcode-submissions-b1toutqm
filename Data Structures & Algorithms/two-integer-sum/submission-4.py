class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap = {}  

        for i in range(len(nums)):
            complement=target-nums[i]
            if nums[i] in prevmap:
                return[prevmap[nums[i]],i]
            else:
                prevmap[complement]=i
