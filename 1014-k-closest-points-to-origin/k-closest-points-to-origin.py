class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # do not need to square root answer
        def dist(x, y):
            return x**2 + y**2
        
        max_heap = []
        for p in points:
            d = dist(p[0], p[1])
            heapq.heappush(max_heap, (-d, p[0], p[1]))
        
        while len(max_heap) > k:
            heapq.heappop(max_heap)
        
        return [[x[1], x[2]] for x in max_heap]