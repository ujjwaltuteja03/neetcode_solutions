class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minh = []
        for x,y in points:
            dist = (x**2) + (y**2)
            minh.append([dist,x,y])
        
        heapq.heapify(minh)
        res = []
        while k>0:
            dist,x,y = heapq.heappop(minh)
            res.append([x,y])
            k-=1
        return res