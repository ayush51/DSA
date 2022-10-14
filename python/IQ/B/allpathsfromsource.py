class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        def dfs(graph, idx, currPath, dest):
            for v in graph[idx]:
                if v == dest:
                    temp = [x for x in currPath]
                    temp.append(v)
                    res.append(temp)
                else:
                    currPath.append(v)
                    dfs(graph, v, currPath, dest)
                    currPath.pop()
        res = []
        dfs(graph, 0, [0], len(graph)-1)
        return res
        
