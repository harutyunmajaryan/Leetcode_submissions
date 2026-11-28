class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        x_list = []
        y_list = []
        output_list = []

        for i in range(0, n, 1):
            x_list.append(nums[i])

        for j in range(n, len(nums), 1):
            y_list.append(nums[j])

        for i, (x, y) in enumerate(zip(x_list, y_list)):
            output_list.append(x_list[i])
            output_list.append(y_list[i])

        return output_list
