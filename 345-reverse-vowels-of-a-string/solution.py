class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set('aeiouAEIOU')  # set で検索を O(1) に
        s_list = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            # 左から母音を探す
            if s_list[left] not in vowels:
                left += 1
                continue

            # 右から母音を探す
            if s_list[right] not in vowels:
                right -= 1
                continue

            # 両方が母音ならswap
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1

        return ''.join(s_list)
