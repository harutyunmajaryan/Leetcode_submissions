class Solution(object):
    def checkTwoChessboards(self, coordinate1, coordinate2):
        """
        :type coordinate1: str
        :type coordinate2: str
        :rtype: bool
        """
        array = ["a","c","e","g"]
        coord1_letter = coordinate1[0]
        coord2_letter = coordinate2[0]
        coord1_number = int(coordinate1[1])
        coord2_number = int(coordinate2[1])

        if (coord1_letter in array and coord2_letter in array) and (coord1_number % 2 == coord2_number % 2):
            return True
        elif ((coord1_letter not in array and coord2_letter in array) or (coord1_letter in array and coord2_letter not in array)) and (coord1_number % 2 != coord2_number % 2):
            return True
        elif (coord1_letter not in array and coord2_letter not in array)  and (coord1_number % 2 == coord2_number % 2):
            return True
        else:
            return False    
        
