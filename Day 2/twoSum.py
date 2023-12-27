class Solution:
    def twoSum(nums,target):
        dic_nums={}

        for i , n in enumerate(nums):
            diff = target - n
            if diff in dic_nums:
                return [i,dic_nums[diff]]
            dic_nums[n] = i



