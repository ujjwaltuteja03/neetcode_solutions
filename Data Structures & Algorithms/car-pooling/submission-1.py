class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        points = []
        for passengers, start, end in trips:
            points.append([start, passengers])
            points.append([end, -passengers])
        
        points.sort()
        curpass = 0
        for point, passengers in points:
            curpass += passengers
            if curpass>capacity: return False
        return True