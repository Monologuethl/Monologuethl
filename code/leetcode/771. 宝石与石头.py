class Solution(object):
    def numJewelsInStones(J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        counter: int = 0
        for s in S:
            for j in J:
                if s == j:
                    counter += 1
        return counter


sl = Solution.numJewelsInStones("aA", "aAAbbbb")
print(sl)

print(ord('a')-97)
print(ord('z')-97)
print(ord('A')-65)
print(ord('Z')-65)