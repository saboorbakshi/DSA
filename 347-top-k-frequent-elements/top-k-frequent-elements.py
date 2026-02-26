class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        l = sorted(hashmap.items(), key = lambda x: x[1], reverse=True)
        return [x[0] for x in l][:k]

            


        