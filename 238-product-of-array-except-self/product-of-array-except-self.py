class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
       # prefixes = [1 for i in range(size)] (another way)
        size = len(nums)
        prefixes = [1] * size
        suffixes = [1] * size
        res = [1] * size

        for i in range(1, size):
            prefixes[i] = prefixes[i - 1] * nums[i - 1]
        
        # stops at i = -1, doesn't execute
        for i in range(size - 2, -1, -1):
            suffixes[i] = suffixes[i + 1] * nums[i + 1]
        
        for i in range(size):
            res[i] = prefixes[i] * suffixes[i]

        print(suffixes)
        print(prefixes)
        return res         