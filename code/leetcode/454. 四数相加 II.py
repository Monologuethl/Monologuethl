class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        res = 0
        record = {}
        for i in A:
            for j in B:
                record[i+j] = record.get(i+j, 0) + 1
        for i in C:
            for j in D:
                temp = 0 - i - j
                if temp in record:
                    res += record[temp]
        return res
        
        