class Solution(object):
    def searchMatrix(self, nums, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        
        row =0
        for i in range(len(nums)):
            if nums[i][-1] < target:
                continue
            elif nums[i][-1] > target:
                row = i
                break
            else:
                return True
        
        l,r = 0 , len(nums[row])-1
        
        while l <= r:
            m = (l+r)//2
            if nums[row][m] < target:
                l = m+1
            elif nums[row][m] > target:
                r = m-1
            else:
                return True
        
        return False
                
        