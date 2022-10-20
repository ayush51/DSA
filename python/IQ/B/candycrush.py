class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        
        if not board:
            board
            
        done = True  #assume my board is good, we return board if done is true, otherwise we call candycrush again if board is unstable
        
        #tag rows
        
        for r in range(len(board)):
            for c in range(len(board[0])-2):  #since window size of 3 so, to not go out of bounds we stop at 3rd last column
                
                num1 = abs(board[r][c])
                num2 = abs(board[r][c+1])
                num3 = abs(board[r][c+2])
                
                if num1 == num2 and num2 == num3 and num1!=0:
                    board[r][c] = -num1
                    board[r][c+1] = -num2
                    board[r][c+2] = -num3
                    done = False
        
        #tag cols
        
        for c in range(len(board[0])):
            for r in range(len(board) - 2):
                num1 = abs(board[r][c])
                num2 = abs(board[r+1][c])
                num3 = abs(board[r+2][c])
                if num1 == num2 and num2 == num3 and num1!=0:
                    board[r][c] = -num1
                    board[r+1][c] = -num2
                    board[r+2][c] = -num3
                    done = False



        
        
        #gravity
        
        if not done:
            for c in range(len(board[0])):
                idx = len(board) - 1 #the first place thats gonna be replaced as here it starts dropping
                
                #move all positive numbers down
                
                for r in range(len(board)-1, -1, -1):
                    if board[r][c] > 0:   #if number is positive, move the number down
                        board[idx][c] = board[r][c]
                        
                        idx -= 1 #moving idx 1 upwards
                        
                        
                        
                #put zeroes in for misisng peices 
                for r in range(idx, -1, -1):
                    board[r][c] = 0
                    
        
        
        return board if done else self.candyCrush(board)
