# Problem

853. Car Fleet

There are n cars going to the same destination along a one-lane road. The destination is target miles away.

You are given two integer arrays, `position` and `speed`, both of length n, where `position[i]` is the position of the ith car, and `speed[i]` is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination.

## Example

```python
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.
The car starting at 0 does not catch up to any other car, so it is a fleet by itself.
The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
Note that no other cars meet these fleets before the destination, so the answer is 3.
```

# Approach

I tackled the Car Fleet problem, which involved determining the number of car fleets that would arrive at a common destination. The challenge was to consider the positions and speeds of the cars, ensuring that a faster car would not overtake a slower one but could form a fleet by driving bumper to bumper.

I approached the problem by creating pairs of position and speed and sorting them in reverse order based on the positions. I used a stack to keep track of the time it would take for each car to reach the destination. If a car catches up to another, it becomes part of the same fleet, and the stack is updated accordingly.

# Code

```python
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p,s) for p,s in zip(position,speed)]
        stack = []

        for p,s in sorted(pairs)[::-1]:
            diff = (target-p)/s
            stack.append(diff)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
```

# How it works

Let's go through an example to illustrate how the provided solution determines the number of car fleets:

```python
target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
```

1. **Initialization:**
   The code creates pairs of position and speed and sorts them in reverse order based on the positions.

2. **Iterating Through Cars:**
   The sorted pairs are iterated, and for each car, the time it takes to reach the destination is calculated (`diff`). This time is added to the stack.

3. **Updating Fleets:**
   If the current car catches up to the car ahead of it, forming a fleet, the stack is updated by popping the last element.

4. **Returning the Result:**
   The function returns the length of the stack, representing the number of car fleets that will arrive at the destination.

In summary, this code efficiently determines the number of car fleets based on the positions and speeds of the cars, considering the constraint that a faster car cannot pass a slower one. The stack is used to track fleet formations, and the final count of fleets is returned.
