#Method 1:

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        i=0
        while i < len(nums):
            if nums[i]==val:
                nums.pop(i)
                i-=1
            i+=1
        
        return len(nums)

nums = [0,1,2,2,3,0,4,2]
val = 2
Solution().removeElement(nums, val)
