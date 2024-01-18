# Problem 

347. Top K Frequent Elements

    Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

## Example

    Input: nums = [1,1,1,2,2,3], k = 2

    Output: [1,2]

# Approach

On day 4, I'm pleased to report that I encountered no challenges with this problem. I successfully devised a solution, and, as usual, I gained additional insights into working with hashmaps in Python.

this code uses a dictionary (freq) to count the frequencies of elements in the input list, and then it iteratively finds and removes the element with the maximum frequency, appending it to the result list. The process repeats for k iterations, resulting in a list of the k most frequent elements.

# Code

```python
    class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = list()
        freq = {}

        for num in nums:
            freq[num] = freq.get(num,0) +1
        
        for i in range(k):
            max_key , max_value = max(freq.items(), key=lambda x:x[1])
            numbers.append(max_key)
            freq.pop(max_key)
        
        return numbers
```

# How it works 

Let's go through an example to illustrate how the provided solution groups anagrams in the given list of integers:

```python
nums = [3, 1, 1, 3, 2, 2, 4, 4, 4, 5, 5]
```

The goal is to find the k most frequent elements. The code achieves this by counting the occurrences of each element using a dictionary. Let's step through the process:

1. **Initialization:**
   ```python
   numbers = list()
   freq = {}
   ```

   This initializes an empty list `numbers` and an empty dictionary `freq`.

2. **Counting Frequencies:**
   The first `for` loop iterates through each element (`num`) in the input list `nums`. For each element, it updates the `freq` dictionary by incrementing the count for that element. The line `freq[num] = freq.get(num, 0) + 1` ensures that if the element is not already in the dictionary, it initializes the count to 0 before incrementing it.

   After processing the example `nums`, the `freq` dictionary would look like this:
   ```python
   {
       3: 2,
       1: 2,
       2: 2,
       4: 3,
       5: 2
   }
   ```

3. **Finding the k Most Frequent Elements:**
   The second `for` loop runs for `k` iterations. In each iteration, it finds the element with the maximum frequency in the current state of the `freq` dictionary using the `max` function with a key function (`lambda x: x[1]` to consider the second element of each tuple, which is the frequency). It appends the found element (`max_key`) to the `numbers` list and removes the element with the maximum frequency from the `freq` dictionary using `pop`.

   After processing the example `nums`, the `numbers` list would contain the k most frequent elements:
   ```python
   [4, 3, 1]
   ```

4. **Returning the Result:**
   The function returns the `numbers` list, which now contains the k most frequent elements.

In summary, this code efficiently identifies the k most frequent elements in the given list of integers by counting the occurrences of each element and selecting the elements with the highest frequencies.


# Another Solution with O(n) time complexity

```python
    class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = [[] for i in range(len(nums) +1)]
        freq = {}

        for num in nums:
            freq[num] = freq.get(num,0) +1
        
        for n,c in freq.items():
            numbers[c].append(n)
        
        res = []
        for i in range(len(numbers) - 1, 0, -1):
            for n in numbers[i]:
                res.append(n)
                if len(res) == k:
                    return res
```
     
    