# Problem

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

## Example

```python
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore, its length is 4.
```

# Approach

On day 8, I tackled the "Longest Consecutive Sequence" problem, which involved finding the length of the longest consecutive sequence of elements in an unsorted array. The challenge was to design an algorithm that runs in O(n) time.

I approached the problem by first converting the given array `nums` into a set `numsSet` to ensure constant time lookups. I then iterated through the unique elements in the set. For each element, I checked if its predecessor (element - 1) was also present in the set. If not, I iterated through consecutive elements (element + 1, element + 2, ...) until no more consecutive elements were found. I maintained a count of the consecutive elements and updated the maximum length (`maxi`) when a longer sequence was encountered.

# Code

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 1
        maxi = 0
        for n in numsSet:
            if n - 1 in numsSet:
                continue
            if n - 1 not in numsSet:
                while (n + 1) in numsSet:
                    longest += 1
                    n = n + 1
            if longest > maxi:
                maxi = longest
            longest = 1
        
        return maxi
```

# How it works

Let's go through an example to illustrate how the provided solution finds the length of the longest consecutive sequence:

```python
nums = [100,4,200,1,3,2]
```

1. **Initialization:**
   The code initializes a set `numsSet` from the given array `nums`.

2. **Iterating Through Unique Elements:**
   The code iterates through the unique elements in `numsSet`. For each element `n`, it checks if `n - 1` is present in `numsSet`. If not, it means `n` is the start of a potential consecutive sequence.

3. **Finding Consecutive Elements:**
   The code enters a `while` loop to find consecutive elements by incrementing `n`. It updates the `longest` variable to keep track of the current sequence length.

4. **Updating Maximum Length:**
   Whenever a longer consecutive sequence is found, the code updates the `maxi` variable.

5. **Returning the Result:**
   After iterating through all unique elements, the function returns the maximum length of consecutive elements (`maxi`).

In summary, this code efficiently finds the length of the longest consecutive sequence in an unsorted array by utilizing a set for constant time lookups. It ensures O(n) time complexity and returns the desired result.