from collections import defaultdict


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        adj = collections.defaultdict(list)
        in_degree = collections.defaultdict(int)
        
        
        for parent, child in edges:
            adj[parent].append(child)
        
            in_degree[child] += 1
            #print(adj)
            #print(in_degree)
            
        queue = deque([node for node in range(n) if node not in in_degree])
        #print(queue)
        
        res = [set() for i in range(n)]
        #print(res)
        
        #res[i] is the nacestors for node i
        
        while queue:
            node = queue.popleft()
        
            
            for child in adj[node]:  #for 3,4 in adj[0]
                res[child].add(node)  #res[3].add(0), res[4].add(0)
                #print(f"res on adding direct parent: {res}")
                
                res[child].update(res[node])
                #print(f"res after adding parent of parent: {res}")
                
                in_degree[child] -= 1
                
                #print(f"indegree after decrement: {in_degree}")
                
                if in_degree[child] == 0:
                    queue.append(child)
                    #print(f"queue: {queue}")
        return [sorted(x) for x in res] 
            
            
            
