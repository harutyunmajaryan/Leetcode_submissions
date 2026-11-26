class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = {}

        for char in s:
            if char not in char_set:
                char_set[char] = 1
            else:
                char_set[char] += 1

        for index, char in enumerate(s):
            if char_set[char] == 1:
                return index  

        return -1

