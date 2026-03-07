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
        
        
def neighbors(adj_matrix , thing):
    neighbors = []
    for i in range(adj_matrix.shape[1]):
        if adj_matrix[thing][i] == 1:
            neighbors.append(i)
            
    return neighbors
            

def dfs(adjacency_matrix , chosen=1):
    visited = {}
    (rows , columns) = adjacency_matrix.shape
    for i in range(columns):
        visited[i] = False 
        
    visited[chosen] = True
    stack = Stack(max_len=adjacency_matrix.shape[1])
    stack.push(chosen)
    
    while(not stack.is_empty()):
        
        j = stack.pop()
        for k in neighbors(adjacency_matrix , j):
            if not visited[k]:
                visited[k] = True 
                stack.push(k)
                
    return visited
                
    
 
    
    




stack = Stack(5)
stack.push(4)
stack.push(4)
print(stack.pop())
print(stack.pop())
print(stack)
print(stack.pop())