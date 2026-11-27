class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = 0
        set_items = {}

        if len(nums) >= 3:
            for num in nums:
                if num not in set_items:
                    set_items[num] = 1
                else:
                    set_items[num] += 1

            if len(set_items) < 3:
                return max(nums)

            nth_max = 0
            for _ in list(nums):
                max_num = max(nums)
                if max_num in set_items:
                    nth_max += 1
                    if nth_max == 3:
                        break
                    count = set_items[max_num]
                    for _ in range(count):
                        nums.remove(max_num)

        elif len(nums) < 3:
            max_num = max(nums)

        return max_num 

            
