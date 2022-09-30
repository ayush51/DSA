class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        a, b = [0] * 8, [0] * 8  #
        for indx in  range(len(moves)):
            row, col = moves[indx]:
                if indx % 2 == 0:
                    player = a
                else:
                    player = b
                player[row] +=1
                player[col + 3] += 1
                if row == col:
                    player[6] += 1
                if row == 2 - col:
                    player[7] += 1
                    
        for i in range(len(a)):
            if a[i] == 3:
                return "A"
            elif b[i] == 3:
                return "B"
        if len(moves) == 9:
            return "Tie"
        else:
            return "pending"
                    # defines chance of which player as a playes at 0, 2, 4, b plays at 1,3,5
        
