class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # count_dict = {}
        # for num in nums:
        #     if count_dict.get(num) == 1:
        #         return True
        #     count_dict[num] = 1
        
        # return False

        if len(set(nums)) < len(nums):
            return True
        return False

        