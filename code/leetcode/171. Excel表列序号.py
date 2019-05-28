class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = 0
        for ch in s:
            n = n*26 + ord(ch)-65+1
        return n