class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = 'aeiouAEIOU'
        s_list = list(s)
        revese_vowels = [char for char in s_list if char in vowels][::-1]
        resolve = ''
        for item in s_list:
            if item in vowels:
                resolve += revese_vowels.pop(0)
            else:
                resolve += item
        return resolve
