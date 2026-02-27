class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        h = min(height[0], height[-1])
        maxArea = h * (n-1)

        i = 0
        j = n-1
        while i < j:
            if height[i] < height[j]:
                i += 1
                while i < j and height[i-1] > height[i]:
                    i +=1
            else:
                j -= 1
                while i < j and height[j+1] > height[j]:
                    j -=1
            w = j - i
            h = min(height[i], height[j])
            maxArea = max(maxArea, w*h)
        
        return maxArea

                

                

        