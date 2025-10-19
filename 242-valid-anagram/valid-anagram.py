class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        dict_s = {}
        dict_t = {}

        for char in s:
            dict_s[char] = dict_s.get(char, 0) + 1
        
        for char in t:
            dict_t[char] = dict_t.get(char, 0) + 1

        return dict_s == dict_t
        
        

        