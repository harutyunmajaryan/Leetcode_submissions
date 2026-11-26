class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        string = s[::-1]
        length = 0
        for char in string:
            if char == " " and length == 0:
                pass
            elif char == " " and length != 0:
                break
            else:
                length += 1

        return length
