class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(r,c):
            if (r < 0 or r == ROWS or
            c < 0 or c == COLS or
            board[r][c] != 'O'):
                return

            board[r][c] = 'T'
            for dr, dc in directions:
                dfs(r+dr, c+dc)

        # Capture unsuronded reagions and turn them to T
        for i in range(ROWS):
            for j in range(COLS):
                if (board[i][j] == 'O' and
                (i in [0, ROWS-1] or j in [0, COLS-1])):
                    dfs(i,j)

        #Convert surrounded reagions to x
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        #Convert T to O
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
