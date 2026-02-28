class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)

        l = 1
        r = max(piles)

        k_arr = []
        while l <= r:
            mid = (l+r) // 2
            hrs = 0
            for p in piles:
                hrs += ceil(p / mid)
            
            if hrs <= h: # mid => k works, wanna see if we can go smaller
                k_arr.append(mid)
                r = mid - 1
            else:
                l = mid + 1
        return min(k_arr)




