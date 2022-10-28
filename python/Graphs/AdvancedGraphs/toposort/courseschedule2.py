class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        prereq = {i: [] for i in range(numCourses)}
        
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        
            
        output = []
        
        cycle, visit = set(), set()
        
        def dfs(crs):
            
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            
            
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            
            visit.add(crs)
            output.append(crs)
            
            return True
        
        for crs in range(numCourses):
            if dfs(crs) == False:
                return []
        return output
