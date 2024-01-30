class Solution(object):
    def trap(self, h):
        """
        :type height: List[int]
        :rtype: int
        """
        if not h : return 0
        sum = 0
        r , l = len(h)-1 , 0
        maxLeft =h[l]
        maxRight= h[r]

        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft , h[l])
                sum += maxLeft-h[l] 
            else:
                r -= 1
                maxRight = max(maxRight,h[r])
                sum += maxRight - h[r]

        return sum       