class MinStack:

    def __init__(self):
        self.mini = []
        self.stack = []

    def push(self, val: int) -> None:
        mn = self.mini[-1] if len(self.mini) else 1<<32
        self.mini.append(min(mn, val))
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.mini.pop()
        

    def top(self) -> int:
        return self.stack[-1] if len(self.stack) else None
        

    def getMin(self) -> int:
        return self.mini[-1] if len(self.stack) else None
        
