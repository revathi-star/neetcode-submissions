class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # n=len(nums)
        # thresh = n//2
        # d={}
        # for i in nums:
        #     if i in d.keys():
        #         d[i]+=1
        #     else:
        #         d[i]=1
        # for (i,v) in d.items():
        #     if v>thresh:
        #         return i
        nums.sort()
        return nums[(len(nums)//2)]
        