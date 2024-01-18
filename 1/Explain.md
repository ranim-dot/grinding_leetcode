# The Problem
    1. Two Sum
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.

## Examples:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Output: Because nums[0] + nums[1] == 9, we return [0, 1].

    Input: nums = [3,2,4], target = 6
    Output: [1,2]
    Output: Because nums[1] + nums[2] == 6, we return [1, 2].

# The Approach
    I figured out that to find two numbers whose sum is equal to the target, I can use a dictionary to keep track of the numbers I have seen so far. 
    While iterating through the array, I calculate the difference between the target and the current number. 
    If this difference is already in the dictionary, I have found the pair that adds up to the target.

# Code

    """
    class Solution:
        def twoSum(self, nums, target):
            dic_nums={}

            for i , n in enumerate(nums):
                diff = target - n
                if diff in dic_nums:
                    return [i, dic_nums[diff]]
                dic_nums[n] = i
    """


# Let's Track what we're doing

## Example usage:

    nums = [2, 7, 11, 15]
    target = 9

1. Initialization:

    dic_nums = {}

2. Iterating through the array nums:

    Iteration 1: n = 2, diff = 7 (9 - 2), dic_nums = {}
   
    Iteration 2: n = 7, diff = 2 (9 - 7), dic_nums = {2: 0}
   
    Found a match! Return [1, 0].

4. The code successfully identifies the indices of the two numbers in the array that add up to the target.
