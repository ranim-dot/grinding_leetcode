class Solution(object):
    def maxArea(self, height):
        res = 0
        i = 0
        j = len(height)-1

        while (i < j):
            if height[i] <= height[j]:
                total = height[i] * (j-i)
                i += 1
            elif height[j] < height[i]:
                total = height[j] * (j-i)
                j -= 1
            if total > res : res = total
        
        return res

        