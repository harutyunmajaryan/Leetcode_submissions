class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        array = []
        for num in range(1,n + 1, 1):
            if num % 5 == 0 and num % 3 == 0:
                num = "FizzBuzz"
                array.append(num)
            elif num % 5 == 0:
                num = "Buzz"
                array.append(num)
            elif num % 3 == 0:
                num = "Fizz"
                array.append(num)
            else:
                array.append(str(num))

        return array                    


        
