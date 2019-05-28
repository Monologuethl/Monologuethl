class Solution(object):
    def uniqueMorseRepresentations(words):
        """
        :type words: List[str]
        :rtype: int
        """
        list_word = []
        string = ""
        s = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
             ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        for word in words:
            for w in word:
                if ord(w) in range(97, 123):
                    index = ord(w)-97
                else:
                    index = ord(w)-65
                print(index)
                string = string+s[index]
            list_word.append(string)
            string = ""
        list_word = list(set(list_word))
        return len(list_word)

sl = Solution.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
print(sl)
