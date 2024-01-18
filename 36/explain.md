# Problem

Given a 9 x 9 Sudoku board, determine if it is valid. Only the filled cells need to be validated according to the following rules:

- Each row must contain the digits 1-9 without repetition.
- Each column must contain the digits 1-9 without repetition.
- Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.

## Example

```python
Input:
board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: True

Input:
board = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: False
```

# Approach

On day 7, I tackled the Sudoku problem, which involved validating a 9 x 9 Sudoku board. The challenge was to ensure that each row, each column, and each of the nine 3 x 3 sub-boxes adhered to the Sudoku rules.

I approached the problem by using three defaultdicts (`rows`, `cols`, and `squares`) to keep track of the numbers present in each row, column, and sub-box, respectively. I iterated through each cell of the board, checking for repetitions based on the rules mentioned above.

# Code

```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[(r//3,c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        
        return True
```

# How it works

Let's go through an example to illustrate how the provided solution validates a Sudoku board:

```python
board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
```

1. **Initialization:**
   The code initializes three defaultdicts (`rows`, `cols`, and `squares`) to keep track of numbers in each row, column, and sub-box.

2. **Iterating Through Cells:**
   The nested `for` loops iterate through each cell in the 9 x 9 board. For each filled cell, the code checks if the number is already present in the corresponding row, column, or sub-box. If a repetition is found, the function returns `False`.

3. **Updating Sets:**
   The code updates the sets in `rows`, `cols`, and `squares` based on the numbers present in the current cell.

4. **Returning the Result:**
   If the entire board is iterated without finding any repetitions, the function returns `True`, indicating that the Sudoku board is valid.

In summary, this code efficiently validates a 9 x 9 Sudoku board by maintaining sets for each row, column, and sub-box. It ensures adherence to the Sudoku rules and returns `True` if the board is valid and `False` otherwise.