class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            if nums[i]>0:
                break
            l=i+1
            r=len(nums)-1

            while l<r:
                threesum=nums[l]+nums[r]+nums[i]
                print(threesum)
                print(nums)
                if threesum>0:
                    r-=1
                elif threesum<0:
                    l+=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1

        return res