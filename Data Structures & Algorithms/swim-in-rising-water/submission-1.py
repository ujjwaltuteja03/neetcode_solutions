class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        minH = [[grid[0][0], 0, 0]]
        # visited.add((0,0))

        while minH:
            t, r, c = heapq.heappop(minH)
            if r == n-1 and c == n-1: return t
            visited.add((r,c))
            for dr, dc in directions:
                nr, nc = r+dr,c+dc
                if (
                    nr<0 or nc<0 or nr>=n or nc>=n
                    or (nr,nc) in visited
                ): continue
                visited.add((nr,nc))
                heapq.heappush(minH, [max(t, grid[nr][nc]), nr, nc])