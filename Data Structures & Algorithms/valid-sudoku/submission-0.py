class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0,len(board)):
            seen_row = set()
            for j in range(0,len(board)):
                cell = board[i][j]
                if cell == ".":
                    continue
                if cell in seen_row:
                    return False
                else:
                    seen_row.add(cell)

        for j in range(0,len(board)):
            seen_col = set()
            for i in range(0,len(board)):
                cell = board[i][j]
                if cell == ".":
                    continue
                if cell in seen_col:
                    return False
                else:
                    seen_col.add(cell)

        for row in range(0,len(board),3):
            for col in range(0,len(board),3):
                seen_board = set()
                for i in range(row,row + 3):
                    for j in range(col, col + 3):
                        cell = board[i][j]
                        if cell == ".":
                            continue
                        if cell in seen_board:
                            return False
                        else:
                            seen_board.add(cell)
        return True

        

        