class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) #key = r//3, c//3

        for r in range(9):

            # r is row is is col
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[r//3,c//3]:

                    # so basically dividing squares in terms of row//3 and col//3, so edge cases is 8//3, 8//3 is 2 thats how we access r,c rightmost in board
                    return False
                       
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[r//3,c//3].add(board[r][c])

        return True   
