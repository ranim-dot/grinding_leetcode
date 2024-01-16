class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {
            ')':'(',
            ']':'[',
            '}':'{' }

        for char in s:
            if char in matches:
                if stack and stack[-1] == matches[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return True if not stack else False
            