class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        available, pending = [], []
        for i, (enqueuetime, processtime) in enumerate(tasks):
            heapq.heappush(pending, (enqueuetime, processtime, i))
        
        time, res = 0, []
        while pending or available:
            while pending and pending[0][0] <= time:
                enqueuetime, processtime, i = heapq.heappop(pending)
                heapq.heappush(available, (processtime, i))
            
            if not available:
                time= pending[0][0]
                continue
            processtime, i = heapq.heappop(available)
            time += processtime
            res.append(i)
        return res