class Solution:
    def wallsAndGates(self, grid: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        rows, cols = len(grid), len(grid[0])
        
        visit = set()
        q = deque()
        
        def addRooms(r,c):
            if (r in range(rows) and
                c in range(cols) and
                (r,c) not in visit and
                gri
      d[r][c] != -1
                ):
                visit.add((r,c))
        
                q.append((r,c))
                
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))
                    
        dist = 0
        
        while q:
            for i in range(len(q)):
                r, c =  q.popleft()
                grid[r][c] = dist
                addRooms(r+1,c)
                addRooms(r-1,c)
                addRooms(r,c+1)
                addRooms(r,c-1)
            dist += 1
