class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        dict_nums = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dict_nums:
                return [i, dict_nums[diff]]
            else:
                dict_nums[nums[i]] = i        