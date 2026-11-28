class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        if len(s) == 0:
            return []

        group = []
        index = 0
        index2 = 0

        for i in range(0, len(s) - 1, 1):
            if i <= len(s) - 1 and s[i] == s[i + 1]:
                index = i
                index2 = i + 1
                for j in range(i + 1, len(s) - 1, 1):
                    if j <= len(s) - 1 and s[j] == s[j + 1]:
                        index2 = j + 2
                    else:
                        break    

                diff = index2 - index + 1
                if diff >= 3:
                    index_group = [index, index2 - 1]
                    group.append(index_group)
                else:
                    pass
            else:
                pass

        seen_second = set()
        filtered = []

        for array in group:
           second_index = array[1]
           if second_index not in seen_second:
              seen_second.add(second_index)
              filtered.append(array)

        group = filtered   
        return group
                    

