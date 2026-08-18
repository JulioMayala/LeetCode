class Solution(object):
    def removeDuplicates(self, nums):
        my_set=set(nums)
        my_list=sorted(my_set)
        for n in range (len(my_list)):
            nums[n]=my_list[n]
        return len(my_set)