class MinStack:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, val: int) -> None:
        if self.stack2 and val <= self.stack2[-1]:
            self.stack1.append(val)
            self.stack2.append(val)
        elif not self.stack2:
            self.stack1.append(val)
            self.stack2.append(val)
        else:
            self.stack1.append(val)
        

    def pop(self) -> None:
        if self.stack1[-1] == self.stack2[-1]:
            self.stack1.pop()
            self.stack2.pop()
        else:
            self.stack1.pop()
        
        

    def top(self) -> int:
        return self.stack1[-1]
        

    def getMin(self) -> int:
        if self.stack2:
            return self.stack2[-1]
        else:
            return 0
        
