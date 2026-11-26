class Solution(object):
    def addDigits(self, num):
        
        sum = 0
        
        if num == 0:
            return 0


        while num > 0:                            # 1. 38 > 0 true  2. 3 > 0 true  3. 11 > 0 true     4. 1 > 0 true
            digit = num % 10                      # 1. digit = 8    2. digit = 3   3. digit = 1       4. digit = 1
            num = num // 10                       # 1. num = 3      2. num = 0     3. num = 1         4. num = 0
            sum += digit                          # 1. sum = 8      2. sum = 11    3. sum = 1         4. sum = 2
            if sum >= 10 and num == 0:         # 1. 8 < 10 false  2. 11 > 10 true  3. sum < 10 false 4. sum <
               num = sum
               sum = 0
            elif sum > 0 and sum <=9 and num == 0:
                return sum
                break 
            else:
                continue      
            

                 
