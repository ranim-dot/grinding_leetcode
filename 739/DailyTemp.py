class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temp)

        for i,v in enumerate(temp):
            while stack and stack[-1][1] < v:
                ipoped,vpoped = stack.pop()
                res[ipoped] = i - ipoped
            stack.append([i,v])
        return res