class Solution(object):
   def twoSum(self, nums, target):
    thisdict={}
    for  i, n in enumerate(nums):
      complement= target - n
      if complement in thisdict:
        self= [thisdict[complement],i]
      else:
        thisdict[n]=i
    return self