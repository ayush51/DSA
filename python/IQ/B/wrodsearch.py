class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visit = set()
        
        def dfs(r,c,i):
            if i == len(word):
                return True #
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                word[i] != board[r][c] or
                (r,c) in visit):
                return False
            
            visit.add((r,c))
            res = (dfs(r+1, c, i+1) or
                   dfs(r-1, c, i+1) or
                   dfs(r, c+1, i+1) or
                   dfs(r, c-1, i+1))
            visit.remove((r,c))
            return res
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False
            
 

SUCCESS: WITHOUT SET
    
    class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
            
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if self.dfs(board, row, col, word):
                        return True
        return False
    def dfs(self, board, row, col, word):
            if not word:
                return True
            ###check validity
            if (0<=row<len(board)) and (0<= col < len(board[0])) and board[row][col] !='#' and board[row][col] == word[0]:
                placeholder = board[row][col]
                board[row][col]="#"
                for row_inc, col_inc in [(0,1), (0,-1), (1,0), (-1,0)]:
                    if self.dfs(board, row+row_inc, col+col_inc, word[1:]):
                        return True
                board[row][col] = placeholder
                return False
        
            
 
