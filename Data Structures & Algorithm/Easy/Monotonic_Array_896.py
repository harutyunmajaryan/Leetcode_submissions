class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        if nums == sorted(nums, reverse = True) or nums == sorted(nums, reverse = False):
            return True
        else:
            return False
