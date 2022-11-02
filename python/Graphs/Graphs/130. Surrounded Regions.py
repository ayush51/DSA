class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows, cols = len(board), len(board[0])
        
        def capturedfs(r,c):
            if ( r < 0 or r == rows  or c < 0 or c == cols or board[r][c] != 'O'):
                return
            
            board[r][c] = 'T'
            
            capturedfs(r+1,c)
            capturedfs(r-1,c)
            capturedfs(r,c+1)
            capturedfs(r,c-1)
            
        #converting border O to T
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and r in [0, rows-1] or c in [0, cols -1]:
                    capturedfs(r,c)
                    
        #convert rest O to X
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                    
                    
        #CONVERT Ts back to O
        
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O';
        
        
        
        
