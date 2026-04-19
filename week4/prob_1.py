class Queue:
    
    def __init__(self):
        self.list = []
        
    def add(self , value):
        self.list.append(value)
        
    def remove(self):
        return self.list.pop(0)
    
    def is_empty(self):
        return len(self.list) == 0

def neighbors(element , Gmat , n):
    return [k for k in range(n) if Gmat[element][k] == 1]
    
def findConnectionLevel(n , Gmat , px , py):
    initial_vertex = px 
    visited = {i : False for i in range(n)}
    distance = {i : float('inf') for i in range(n)}
    
    visited[initial_vertex] = True 
    distance[initial_vertex] = 0 
    queue = Queue()
    queue.add(initial_vertex)
    
    while not queue.is_empty():
        
        element = queue.remove()
        
        if element == py:
            return distance[py]
        
        for neighbor in neighbors(element , Gmat , n):
            if not visited[neighbor]:
                distance[neighbor] = distance[element] + 1 
                visited[neighbor] = True 
                queue.add(neighbor)
                
    return 0
            
    
