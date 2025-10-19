class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # create dictionary of num -> freq
        dict_nums = {}
        for num in nums:
            dict_nums[num] = dict_nums.get(num, 0) + 1
        
        # create array of freq -> [num]
        # +1 here because each index corresponds to a frequency
        # max freq value = len(num), so must have an index = len(num)
        freq_list = [[] for i in range(len(nums) + 1)]
        for num, freq in dict_nums.items():
            freq_list[freq].append(num)
        
        # iterate over arry and return first k elements
        res = []
        for i in range(len(freq_list) - 1, 0, -1):
            for num in freq_list[i]:
                res.append(num)
                if len(res) == k:
                    return res

            


        