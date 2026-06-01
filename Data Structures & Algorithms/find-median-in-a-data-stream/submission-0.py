class MedianFinder:

    def __init__(self):
        #small=maxheap, large=minheap
        #all elements in small * -1 for max heap when pushing/popping
        # largest in small and/or smallest in large (top in both cases)
        # give us the median
        self.small, self.large =[], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1*num)

        #every num in small <= every num in large
        if (self.small and self.large and (-1 * self.small[0] > self.large[0])):
            val=-1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        #mainting difference of 1 in length  
        if len(self.small) > len(self.large)+1:
            val=-1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.small)+1 < len(self.large):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1* val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1*self.small[0]
        if len(self.small) < len(self.large):
            return self.large[0]
        return (-1*self.small[0] + self.large[0])/2