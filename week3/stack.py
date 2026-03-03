class Stack:
    
    def __init__(self):
        self.array = []
        
    def push(self , data):
        try:
            self.array.append(data)
        except Exception:
            return "An unexpected error has occured"
        
    def pop(self):
        if not self.is_empty():
           return self.array.pop()    
        return "stack is empty"
    
    def peek(self):
        if not self.is_empty():
            return self.array[-1]
        return "Stack is empty"
        
    def is_empty(self):
        return True if len(self.array) == 0 else False