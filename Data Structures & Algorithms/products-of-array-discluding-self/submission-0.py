class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]
        suffix=[1]*len(nums)
        for i in range(len(nums)-1):
            prefix.append(nums[i]*prefix[i])
        #return prefix
        
        for i in range(len(nums)-2,-1,-1):
            suffix[i]=suffix[i+1]*nums[i+1]
        #return suffix

        for i in range(len(prefix)):
            prefix[i]*=suffix[i]
        return prefix

