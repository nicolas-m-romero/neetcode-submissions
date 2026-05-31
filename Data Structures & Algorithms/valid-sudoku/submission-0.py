class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                tile = board[r][c]
                if tile == ".":
                    continue

                if (   tile in rows[r]
                    or tile in cols[c]
                    or tile in squares[(r//3,c//3)]):
                    return False

                rows[r].add(tile)
                cols[c].add(tile)
                squares[(r//3,c//3)].add(board[r][c])

        return True