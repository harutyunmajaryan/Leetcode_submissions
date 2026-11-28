class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for num in nums[:]:
            if num == val:
                nums.remove(num)

        return len(nums)       
        
