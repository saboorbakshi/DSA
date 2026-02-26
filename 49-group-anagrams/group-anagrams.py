class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        """
        defaultdict(list) creates a dictionary where each new key automatically starts with an empty list as its default value
        tuples are hashable. Lists and dictionaries are not in hashmaps.
        """
        newList = []
        for s in strs:
            newList.append(''.join(sorted(s)))
        
        hashmap = {}
        for index, sortedS in enumerate(newList):
            hashmap.setdefault(sortedS, []).append(index)

        return [[strs[i] for i in indices] for indices in hashmap.values()]


            





        