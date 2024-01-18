# Problem

1624. Largest Substring Between Two Equal Characters

Given a string `s`, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring, return -1. A substring is a contiguous sequence of characters within a string.

## Example

```python
Input: s = "abca"
Output: 2
Explanation: The substring between the two 'a's is "b", and its length is 2.
```

# Approach

On day 6, I faced a challenge in understanding the problem requirements and constraints, but I successfully devised a solution after careful analysis. The problem involves finding the length of the longest substring between two equal characters in a given string.

The approach I used involves maintaining a dictionary (`indices`) to store the last index at which each character appears. While iterating through the string, if a character is already in `indices`, I update a variable (`max_length`) by comparing it with the difference between the current index and the last index of that character, minus 1 (to exclude the two characters). The final result is the length of the longest substring between two equal characters. If no such substring is found, `max_length` remains -1.

# Code

```python
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        indices = {}  # Dictionary to store the last index of each character
        max_length = -1

        for i, ch in enumerate(s):
            if ch in indices:
                max_length = max(max_length, i - indices[ch] - 1)
            else:
                indices[ch] = i

        return max_length
```

# How it works

Let's go through an example to illustrate how the provided solution determines the length of the longest substring between two equal characters in the given string:

```python
s = "abca"
```

The goal is to find the length of the longest substring between two equal characters. The code achieves this by maintaining a dictionary (`indices`) to store the last index at which each character appears. Let's step through the process:

1. **Initialization:**
   ```python
   indices = {}
   max_length = -1
   ```

   This initializes an empty dictionary `indices` and a variable `max_length` with an initial value of -1.

2. **Iterating Through the String:**
   The `for` loop iterates through each character (`ch`) in the input string `s`. For each character, it checks if the character is already in the `indices` dictionary. If it is, the code updates `max_length` by comparing it with the difference between the current index (`i`) and the last index of that character (`indices[ch]`), minus 1 (to exclude the two characters). If the character is not in `indices`, it adds the character to the dictionary with its current index.

   After processing the example `s`, the `indices` dictionary would look like this:
   ```python
   {
       'a': 3,
       'b': 1,
       'c': 2
   }
   ```

   The `max_length` variable would be updated during the iterations, and its final value represents the length of the longest substring between two equal characters.

3. **Returning the Result:**
   The function returns the `max_length`, which represents the length of the longest substring between two equal characters in the given string.

In summary, this code efficiently determines the length of the longest substring between two equal characters in a given string by maintaining a dictionary to store the last index of each character and updating a variable to track the maximum length.