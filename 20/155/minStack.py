class MinStack:
    def __init__(self):
        self.stack = []
        self.min = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min:
            if val <= self.min[-1]:
                self.min.append(val)
        else:
            self.min.append(val)
        

    def pop(self) -> None:
        if self.stack:
            if self.stack[-1] == self.min[-1]:
                del self.min[-1]
            del self.stack[-1]

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None 

    def getMin(self) -> int:
        return self.min[-1]