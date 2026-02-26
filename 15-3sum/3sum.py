class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        # ans2 = []
        n = len(nums)
        nums.sort()
        for i in range(n):
            if nums[i] > 0: # impossible for summ == 0
                break
            elif i > 0 and nums[i] == nums[i-1]:
                continue

            # offset = nums[i]
            # target = nums[i] * -1
            lo = i+1
            hi = n-1
            while lo < hi:
                summ = nums[i] + nums[lo] + nums[hi]
                if summ == 0:
                    # ans2.append([i, lo, hi])
                    ans.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi+1]:
                        hi -= 1
                elif summ > 0:
                    hi -= 1
                    while lo < hi and nums[hi] == nums[hi+1]:
                        hi -= 1
                else:
                    lo += 1
                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo += 1
        # print(nums)
        # print(ans2)
        return ans



        