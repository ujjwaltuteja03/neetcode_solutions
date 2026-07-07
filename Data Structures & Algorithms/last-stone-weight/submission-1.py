class Solution:
    # use max heap to get largest values, if the difference
    # is 0, move on, if not, push new value back into the heapq

    # always push and pop negative of the values in a maxheap in python
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones)>1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            cur = first-second
            if cur:
                heapq.heappush(stones, cur)
        
        return abs(stones[0]) if stones else 0