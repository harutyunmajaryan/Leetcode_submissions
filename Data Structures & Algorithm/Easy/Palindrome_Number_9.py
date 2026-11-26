class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        s = str(x)
    
        for index, digit in enumerate(s):
            if digit != s[len(s) - index - 1]:
                    return False
        return True

