input = [[1,2,3],[3,1,2],[2,3,1]]

def checkValid(matrix: List[List[int]]) -> bool:
    row, col = defaultdict(set), defaultdict(set)
    
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] in row[r] or matrix[r][c] in col[c]:
                return False
            row[r].add(matrix[r][c])
            col[c].add(matrix[r][c])
    return True

print(checkValid(input))
