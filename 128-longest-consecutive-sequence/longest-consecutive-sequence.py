class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        uniqueNums = set(nums)
        
        startNums = []
        for num in uniqueNums:
            if num-1 not in uniqueNums: #O(1)
                startNums.append(num)
        
        maxCount = 1
        for num in startNums:
            count = 1
            while num+count in uniqueNums:
                count += 1
            if count > maxCount:
                maxCount = count
        
        return maxCount




        





        