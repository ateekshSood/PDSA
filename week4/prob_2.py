from collections import deque

class Stack:
    
    def __init__(self):
        self.stack = deque()
        
    def push(self , value):
        self.stack.append(value)
        
    def pop(self):
        return self.stack.pop()
    
    def isEmpty(self):
        return len(self.stack) == 0


def rundfs(adj_list , tank , visited , tanks):
    visited[tank] = True 
    stack = Stack()
    stack.push(tank)
    
    while not stack.isEmpty():
        
        element = stack.pop()
        for k in adj_list[element]:
            if not visited[k]:
                visited[k] = True 
                stack.push(k) 



def findMasterTank(tanks , pipes):
    
    adj_list = {tank : [] for tank in tanks}
    for (i,j) in pipes:
        adj_list[i].append(j)
        
    visited = {tank : False for tank in tanks}
    last_visited = tanks[0]
    
    for tank in tanks:
        if not visited[tank]:
            rundfs(adj_list , tank , visited , tanks)
            last_visited = tank 
            
    visited = {tank : False for tank in tanks}
    rundfs(adj_list , last_visited , visited , tanks)
    
    for i in visited:
        if not visited[i]:
            return 0 
    
    return last_visited
        