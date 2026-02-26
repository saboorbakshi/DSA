class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        i = 0
        j = n - 1
        while i < n and j > 0 and i != j:
            s = numbers[i] + numbers[j]
            if target == s:
                return [i+1, j+1]
            elif target > s:
                i += 1
            else:
                j -= 1
            

            

            

