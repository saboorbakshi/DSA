class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        """
        defaultdict(list) creates a dictionary where each new key automatically starts with an empty list as its default value
        """
        
        dict_strs = {}
        for s in strs:
            counts = [0] * 26
            for char in s:
                counts[ord(char) - ord('a')] += 1
            dict_strs.setdefault(tuple(counts), []).append(s)

        return list(dict_strs.values())
        