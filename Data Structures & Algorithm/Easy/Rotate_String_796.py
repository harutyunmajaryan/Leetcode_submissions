class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        status = False
        if s == goal:
            status = True
        if s[::-1] == goal:
            status = False


        for i in range(0,len(s), 1):
            if s[(i+1):] + s[0:(i+1)] == goal:
                status = True
                break

        return status
