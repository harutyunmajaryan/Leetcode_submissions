class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        index = -1
        for i in range(0, len(haystack) - len(needle) + 1, 1):
            if haystack[i:len(needle) + i] == needle:
                index = i
                return index
                break

        return index
