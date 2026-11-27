class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        set_items = {}
        for num in nums:
            if num not in set_items:
                set_items[num] = 1
            else:
                set_items[num] += 1
        
        status = False
        for num in nums:
            if set_items[num] > 1:
                status = True
            else:
                pass

        return status
