# https://leetcode.com/problems/valid-sudoku/
# 36. Valid Sudoku
# Medium
# 10.1K
# 1K
# Companies
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
 

# Example 1:


# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
# Example 2:

# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.

import math as m


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        row = {}
        col = {}
        sub = {}
        for i in range(len(board)):
            r = m.floor(i / 3)
            if i not in row:
                row[i] = []
            for j in range(len(board)):
                if j not in col:
                    col[j] = []
                num = board[i][j]
                if num == '.':
                    continue
                num = int(num)
                if num < 1 or num > 9:
                    continue
                if num in row[i] or num in col[j]:
                    return False
                row[i].append(num)
                col[j].append(num)
                c =  m.floor(j / 3)
                if (r,c) not in sub:
                    sub[(r,c)]= [num]
                elif num in sub[(r,c)]:
                    return False
                else:
                     sub[(r,c)].append(num)
        return True

        

if __name__ == '__main__':
    s = Solution()
    t =  [
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".","6",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".","8",".",".",".","."],
    ["9",".",".",".","7","5",".",".","."],
    [".",".",".",".","5",".",".","8","."],
    [".",".","9",".",".",".",".",".","."],
    ["2",".","6",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."]]
    res = s.isValidSudoku(t)
    print(res)