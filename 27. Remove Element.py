class Solution(object):
    def removeElement(self, nums, val):
        x=[]
        value=0
        for n in nums:
            if n != val:
                value+=1
                x.append(n)
        for n in range(len(x)):
            nums[n]=x[n]
        return value