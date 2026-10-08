class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # l=[]
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             l=l+[i,j]
        #             return l   
        # return l
        for i,v in enumerate(nums):
            for j,w in enumerate(nums[i+1:]):
                if v+w==target:
                    return [i,j+i+1]
        return []
