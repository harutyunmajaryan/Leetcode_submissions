class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        integer_string = ""
        for num in digits:
            integer_string += str(num)     #"123"

        integer_int = int(integer_string)         #123
        new_integer_str = str(integer_int + 1)   #"124"
        list = []

        for char in new_integer_str:
            list.append(int(char))  #[1,2,4]

        return list    


