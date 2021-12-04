class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            Answer = target - nums[i]
            if Answer in nums[i+1:]:
                print (i , nums.index(Answer))
                return ([i, nums[i+1:].index(Answer)])
            
                
              
            