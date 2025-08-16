
class BackTrack:

    def exist(Self, board: list[list[str]], word: str) -> bool:
        ROWS, COLS, LEN = len(board), len(board[0]), len(word)
        print('BOARD SIZE=', (ROWS, COLS), 'word=', LEN)
        if ROWS < LEN and COLS < LEN:  # check wether the board row or col size can build the word
            print('word cannbot be built, size higher then the max')
            return False

        path = set()

        def dfs(r, c, i):
            print('look at ', (r, c, i))
            if i == LEN:
                return True
            if (
                    r < 0 or c < 0  # before first char in a row, or above first char in a column
                    or r >= ROWS or c >= COLS  # after last char in a row, or below of last char in a column
                    or word[i] != board[r][c]  # not matching char
                    or (r, c) in path  # already visited char
            ):
                return False

            path.add((r, c))  # keep track of this cell
            print('#', (r, c))
            # look for the next char at the 4 adjacent positions
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            path.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
            return False


bt = BackTrack()
board = [
    ['x', 'z', 'z', 'a', 'b'],
    ['a', 'a', 'c', 'x', 'y'],
    ['b', 'b', 'x', 'y', 'a'],
    ['x', 'c', 'a', 'a', 'y'],
    ['z', 'x', 'y', 'z', 'b']
]
res = bt.exist(board=board, word='xyz')
print('result = ', res)
