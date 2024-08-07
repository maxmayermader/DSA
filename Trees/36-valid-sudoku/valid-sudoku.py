class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        grid = defaultdict(set)

        print(row)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                elif (board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in grid[i // 3, j // 3]):
                    return False
                else:
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    grid[i//3, j//3].add(board[i][j])
        return True