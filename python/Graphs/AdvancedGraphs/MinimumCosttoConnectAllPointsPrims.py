class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        
        N  = len(points)
        
        adj = { i : [] for i in range(N)}  # i : list of [cost, neighbours]
        
        print(adj)
        
        for i in range(N):##
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])  #cz undirected so both neighbour possible
                
                
        #PRIM
        
        cost = 0
        visit = set()
        minH = [[0,0]] #cost, node
        
        while len(visit) < N:
            icost, i = heapq.heappop(minH) 
            if i in visit:
                continue
            
            cost += icost
            print(cost)
            visit.add(i)
            
            for necost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH, [necost, nei])
                    
        return cost
        
