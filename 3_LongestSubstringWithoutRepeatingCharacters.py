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
                ix = sub_list.index(char)
                sub_list = sub_list[ix+1:] + [char]

        if len(sub_list) > longest:
            longest = len(sub_list)
        
        return longest
