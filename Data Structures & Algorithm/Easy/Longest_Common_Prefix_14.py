class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        first = strs[0]
        second = strs[1]
        match_len = 0

        for p1, p2 in zip(first, second):
            if p1 == p2:
                match_len += 1
            else:
                break

        prefix = first[:match_len]
        if not prefix:
            return ""

        for string in strs[2:]:
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix
         
