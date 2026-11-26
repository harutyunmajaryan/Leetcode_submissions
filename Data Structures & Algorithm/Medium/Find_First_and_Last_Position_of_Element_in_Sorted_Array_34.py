class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        index_array = []
        status_count = 0


        if len(nums) == 0:
            return [-1,-1]
        else:
            for index, number in enumerate(nums):
                if number == target:
                     index_array.append(index)
                     status_count += 1


            if status_count == 0:
                return [-1,-1]
            else:
                return index_array           #this array will contain all the indecies where the target matches a number from nums    


