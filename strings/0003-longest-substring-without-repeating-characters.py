class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub_list = []
        longest = 0
        for char in s:
            if char not in sub_list:
                sub_list.append(char)
            else:
                if len(sub_list) > longest:
                    longest = len(sub_list)
                sub_list = sub_list[sub_list.index(char)+1:] + [char]

        if len(sub_list) > longest:
            longest = len(sub_list)
        
        return longest

# Runtime: 28 ms, beats 35.67% of solutions
# Memory: 12.42 MB, beats 96.29% of solutions
