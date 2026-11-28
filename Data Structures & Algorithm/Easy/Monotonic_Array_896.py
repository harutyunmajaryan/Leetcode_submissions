class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #the run time is too much for this therefore there are some ways to optimzise the algorithm
        if nums == sorted(nums, reverse = True) or nums == sorted(nums, reverse = False):
            return True
        else:
            return False
