class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        prefixes = [1] * length #left
        suffixes = [1] * length #right
        for i in range(1, length):
            j = length - i - 1
            prefixes[i] = nums[i - 1] * prefixes[i - 1]
            suffixes[j] = nums[j + 1] * suffixes[j + 1]
            # if i == 0:
            #     prefixes[i] = 1
            #     suffixes[i] = 1
        return [prefixes[i] * suffixes[i] for i in range(length)]
        
        

            

            