class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # O(n^2)
        # for index, num in enumerate(nums):
        #     diff = target - num
        #     for index2, num2 in enumerate(nums):
        #         if index != index2 and diff == num2:
        #             return [index, index2]
        
        hashmap = {}
        for index, num in enumerate(nums):
            hashmap[num] = index
        
        for index, num in enumerate(nums):
            diff = target - num
            if hashmap.get(diff) and index != hashmap.get(diff):
                return [hashmap[diff], index]
        



        



