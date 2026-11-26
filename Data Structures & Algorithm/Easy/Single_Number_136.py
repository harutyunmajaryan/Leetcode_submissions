class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return  None

        map = {}
        for num in nums:
            if num not in map:
                map[num] = 1    
            else:
                map[num] += 1

        desired_number = None
        for num in map:
            if map[num] == 1:
                desired_number = num
                break
            else:
                pass


        return desired_number
