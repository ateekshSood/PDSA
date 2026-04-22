class Queue:
    
    def __init__(self):
        self.queue = []
        
    def add(self , value):
        self.queue.append(value)
        
    def remove(self):
        return self.queue.pop(0)
    
    def is_empty(self):
        return len(self.queue) == 0 

def bfs(AList):
    
    visited = {key : False for key in AList.keys()}
    queue = Queue()
    queue.add(0)
    visited[0] = True 
    
    while not queue.is_empty():
        
        element = queue.remove()
        
        if not visited[element]:
            
            for node in AList[element]:
                if not visited[node]:
                    visited[node] = True 
                    
                    
    return [key for key in AList.keys() if not visited[key]]
    


def find_missing_node(AList):
    
    return bfs[AList]