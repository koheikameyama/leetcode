class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        word1List = list(word1)
        word2List = list(word2)
        word1Length = len(word1)
        word2Length = len(word2)

        maxLength = max(word1Length, word2Length)
        result = ''
        for index in range(maxLength):
            if 0 <= index < word1Length:
                result += word1[index]
            if 0 <= index < word2Length:
                result += word2[index]
        return result
