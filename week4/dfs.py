import numpy 

class Stack:
    
    def __init__(self , max_len):
        self.stack = []
        self.max_len = max_len
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def is_full(self):
        return len(self.stack) == self.max_len
    
    def push(self , data):
        if not self.is_full():
            self.stack.append(data)
        else:
            raise IndexError("The stack is full")
    
    def pop(self):
        if not self.is_empty():
            element = self.stack.pop()
            return element
        else:
            raise IndexError("The stack is empty")
        
    def __str__(self):
        return str(self.stack)
        print(stack.pop())
        
        
  



stack = Stack(5)
stack.push(4)
stack.push(4)
print(stack.pop())
print(stack.pop())
print(stack)
print(stack.pop())