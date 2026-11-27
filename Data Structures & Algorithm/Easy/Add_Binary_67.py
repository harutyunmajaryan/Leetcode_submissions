class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        val_a = 0
        val_b = 0

        for index, char in enumerate(a[::-1]):
            if int(char) == 1:
                val_a += pow(2, index)
            else:
                pass    
        
        for index, char in enumerate(b[::-1]):
            if int(char) == 1:
                val_b += pow(2, index)
            else:
                pass

        total = val_a + val_b
        new_binary = ""
        if total == 0:
            return "0"
        
        while total > 0:
            new_binary = str(total % 2) + new_binary
            total //= 2

        return new_binary   

