# Problem

739. Daily Temperatures

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

## Example

```python
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```

# Approach

I tackled the Daily Temperatures problem, where the goal was to find the number of days one has to wait for a warmer temperature. The challenge was to efficiently calculate these waiting days based on the given daily temperatures.

I approached the problem using a stack to keep track of the indices of temperatures. The stack maintained decreasing order of temperatures, and for each temperature encountered, I checked if it could be the next warmer day for the temperatures stored in the stack.

# Code

```python
class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temp)

        for i, v in enumerate(temp):
            while stack and stack[-1][1] < v:
                popped_index, popped_value = stack.pop()
                res[popped_index] = i - popped_index
            stack.append([i, v])
        return res
```

# How it works

Let's go through an example to illustrate how the provided solution calculates the waiting days for a warmer temperature:

```python
temperatures = [73,74,75,71,69,72,76,73]
```

1. **Initialization:**
   The code initializes an empty stack to store the indices and values of temperatures and a list `res` to store the waiting days.

2. **Iterating Through Temperatures:**
   The `for` loop iterates through each temperature in the given array. For each temperature, it checks whether it is warmer than the temperatures in the stack.

3. **Updating Waiting Days:**
   If a warmer temperature is found, the code pops the temperatures from the stack and calculates the waiting days for the popped temperatures. The waiting days are then updated in the `res` list.

4. **Stack Maintenance:**
   The stack maintains a decreasing order of temperatures, ensuring an efficient way to find the next warmer day.

5. **Returning the Result:**
   The final result is a list (`res`) where each element represents the number of days one has to wait for a warmer temperature after the corresponding day.

In summary, this code efficiently calculates the waiting days for a warmer temperature by using a stack to keep track of temperatures in decreasing order. It iterates through the given temperatures, updates the waiting days, and returns the result in the `res` list.