class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def isPalindrome(s):
            for i in range(len(s)//2):
                if s[i] is not s[len(s) - i - 1]:
                    return False
            return True

        result = s[0]
        for i1, char1 in enumerate(s):
            # end early if longer palindrome is not possible
            if len(result) >= len(s) - i1 + 1:
                return result
            
            temp = char1
            for char2 in s[i1 + 1:]:
                temp += char2
                if char2 == char1 and len(temp) > len(result) and isPalindrome(temp):
                    result = temp

        return result

# Runtime: 3855 ms, beats 21.03% of solutions
# Memory: 12.44 MB, beats 79.44% of solutions
