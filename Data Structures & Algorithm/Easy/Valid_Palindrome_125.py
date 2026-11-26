class Solution(object):
    def isPalindrome(self, s):
        # Remove non-alphanumeric characters and lowercase
        clean_s = ''.join(c.lower() for c in s if c.isalnum())
        return clean_s == clean_s[::-1]

sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))


