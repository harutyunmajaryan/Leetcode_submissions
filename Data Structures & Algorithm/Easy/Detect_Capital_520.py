class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        string = word[0].upper() + word[1:].lower()
        if word == word.upper():
            return True
        elif word == word.lower():
            return True
        elif word == string:
            return True
        else:
            return False
