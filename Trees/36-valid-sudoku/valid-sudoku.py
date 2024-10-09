class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        diags = defaultdict(set)
        
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != '.':
                    if (board[i][j] in rows[i] or
                        board[i][j] in cols[j] or
                        board[i][j] in diags[(i//3, j//3)]):
                        return False

                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    diags[((i//3), (j//3))].add(board[i][j])

        return True
                    