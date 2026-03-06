import numpy as np 
from typing import TypeVar, Generic, Optional

# define a generic type variable 'T'
T = TypeVar('T')
class Queue(Generic[T]):
    def __init__(self) -> None:
        # using a standard python list to store the generic items
        self._queue: list[T] = []

    def add(self, item: T) -> None:
        """adds an item to the back of the queue."""
        self._queue.append(item)

    def remove(self) -> Optional[T]:
        """removes and returns the item from the front of the queue."""
        if self.is_empty():
            print("queue is empty!")
            return None
        # pop(0) removes the first element from the standard list
        return self._queue.pop(0)

    def peek(self) -> Optional[T]:
        """returns the front item without removing it."""
        if self.is_empty():
            print("queue is empty!")
            return None
        return self._queue[0]

    def is_empty(self) -> bool:
        """checks if the queue has any items."""
        return len(self._queue) == 0

def make_adjacency_matrix(shape : int):
        
    rng = np.random.default_rng(42)
    x1 = (rng.random((shape ** 2)) * 2).round(0).astype(np.int32)
    x2 = (rng.random((shape ** 2)) * 2).round(0).astype(np.int32)

    points = np.column_stack((x1, x2))
    adjacency_matrix = np.zeros((shape,shape))

    for i in range(points.shape[0]):
        i , j = points[i , 0] , points[i , 0]
        adjacency_matrix[i , j] = 1
        
    return adjacency_matrix

def neighbours(adjacency_matrix , row , columns):
    neighbors = []
    for i in range(columns):
        if adjacency_matrix[row][i] == 1:
            neighbors.append(i)
            
    return neighbors



def bfs(adj_matrix):
    inital_vertex = 1 
    visited = {}
    
    (row , column) = adj_matrix.shape
    for i in range(column):
        visited[i] = False 
        
    
    visited[inital_vertex] = True 
    queue = Queue[int]()
    queue.add(inital_vertex)
    
    while(not queue.is_empty()):
        j = queue.remove()
        for k in neighbours(adj_matrix , j , column):
            if (not visited[k]):
                visited[k] =  True
                queue.add(k)
                
    return visited
    


adj_matrix = np.array([[0,1,1],[1,0,0],[1,0,0]])

print(adj_matrix)
print(bfs(adj_matrix))