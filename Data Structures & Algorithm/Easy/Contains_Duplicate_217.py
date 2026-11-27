class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        #I created a set of numbers where keys are the numbers in the list and the values are the number of occurances of those numbers:
        #Then you need to check if there is any key that contains a number > 1 if yes then change the status to True of not then return the default status = False
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
