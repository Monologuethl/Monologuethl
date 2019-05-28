class Solution(object):
    def numberOfLines(widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        print(ord('c')-ord('a'))
        total = 0
        count = 0
        tmp = len(S)
        i = 0
        while i < tmp:
            index = ord(S[i])-ord('a')
            total += widths[index]
            if total == 100:
                total = 0
                count += 1
            if total > 100:
                count += 1
                total = 0
                i -= 1
            i += 1
        if total > 0:
            count += 1
        return [count, total]


sl = Solution.numberOfLines(
    [4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    "bbbcccdddaaa")
print(sl)
