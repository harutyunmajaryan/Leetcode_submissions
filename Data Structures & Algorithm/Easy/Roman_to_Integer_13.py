class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sum = 0

#first iteration is written in pseudocode
        for index, letter_in_s in enumerate(s):                  # index = 0, letter_in_s = "I"
          if index < len(s) - 1:                                 # if 0 < 2 true
            if s[index] in map and s[index + 1] in map:          #if s[0], so I is in map so true and s[0 + 1],so I is in map so true
                if map[s[index]] < map[s[index + 1]]:            #if map[s[0]] < map[s[1]], so map["I"] < map["I"], 1 < 1 so false
                    sum -= map[s[index]]                          #skip 
                elif map[s[index]] == map[s[index + 1]]:         #elif map[s[1]] <= map[s[0]], so map["I"] <= map["I"], 1<=1, so true
                    sum += map[s[index]]                           #sum = 1 + 0 = 1
                elif map[s[index]] > map[s[index + 1]]:
                    sum += map[s[index]]
            else:
                break
          elif index == len(s) - 1:
                    sum += map[s[index]]

        return sum


