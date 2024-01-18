# Problem

**22. Generate Parentheses**

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

## Example

```python
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

# Approach

On day 11, I tackled the Generate Parentheses problem, which involved generating all combinations of well-formed parentheses given the number of pairs, `n`. The challenge was to explore all possible combinations while ensuring the parentheses are balanced.

I approached the problem using backtracking, a common technique for generating all possible solutions to a problem. The main idea was to explore different choices for placing open and closed parentheses and backtrack when necessary.

# Code

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtracking(openN, closedN):
            if closedN == openN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtracking(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtracking(openN, closedN + 1)
                stack.pop()

        backtracking(0, 0)
        return res
```

# How it works

Let's go through an example to illustrate how the provided solution generates all combinations of well-formed parentheses for `n = 3`:

```python
n = 3
```

1. **Initialization:**
   The code initializes an empty stack (`stack`) to keep track of the current combination and an empty list (`res`) to store the final result.

2. **Backtracking Function:**
   The `backtracking` function is defined to explore different choices for placing open and closed parentheses. It takes two parameters, `openN` and `closedN`, representing the count of open and closed parentheses placed so far.

3. **Base Case:**
   If the count of both open and closed parentheses equals `n`, it means a valid combination is formed, and it is added to the result (`res`).

4. **Choice:**
   The code considers two choices:
   - If the count of open parentheses (`openN`) is less than `n`, it appends an open parenthesis to the stack and makes a recursive call with increased `openN`.
   - If the count of closed parentheses (`closedN`) is less than `openN`, it appends a closed parenthesis to the stack and makes a recursive call with increased `closedN`.

5. **Backtrack:**
   After exploring a choice, the code backtracks by popping the last element from the stack to try other possibilities.

6. **Calling Backtracking:**
   The `backtracking` function is initially called with `openN = 0` and `closedN = 0` to start the exploration.

7. **Returning the Result:**
   The function returns the final result, which is a list of all combinations of well-formed parentheses.

In summary, this code efficiently generates all combinations of well-formed parentheses for a given number of pairs, `n`, using backtracking. It explores different choices, ensures the parentheses are balanced, and returns a list of valid combinations.