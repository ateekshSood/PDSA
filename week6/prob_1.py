class min_heap:
    
    def __init__(self):
        self.arr = []
        
    def heapify_up(self):
        i = len(self.arr) - 1 
        
        while i > 0:
            p = (i - 1)//2 
            
            if self.arr[i][0] < self.arr[p][0]:
                (self.arr[i] , self.arr[p]) = (self.arr[p] , self.arr[i])
                i = p 
            else:
                break 
            
    def insert(self , value):
        self.arr.append(value)
        self.heapify_up()
        
    def heapify_down(self , index):
        
        n = len(self.arr)
        i = index 
        
        while i< n :
            smallest = i 
            left_child = 2 * i + 1 
            right_child = 2 * i + 2
            
            if left_child < n and self.arr[left_child][0] < self.arr[smallest][0]:
                
                smallest = left_child 

                
            if right_child < n and self.arr[right_child][0] < self.arr[smallest][0]:
                smallest = right_child 

                
            if smallest != i:
                (self.arr[i] , self.arr[smallest]) = (self.arr[smallest] , self.arr[i])
                i = smallest
            else:
                break 
        
        
    def delete_min(self):
        
        min = self.arr[0]
        last_element = self.arr.pop()
        
        if len(self.arr) > 0:
            self.arr[0] = last_element
            self.heapify_down(0)
            
        return (min[0] , min[1] , min[2])
        
    def is_empty(self):
        return len(self.arr) == 0
        
def mergeKLists(L):
    
    heap = min_heap()
    
    for i in range(len(L)):
        if len(L[i]) > 0:
            heap.insert((L[i][0] , i , 0) )  # insert first element of every list
        
    final_list = []
    while not heap.is_empty():
        min_element , list_index , posi = heap.delete_min()
        final_list.append(min_element)
        
        if posi + 1 < len(L[list_index]):
        
            heap.insert((L[list_index][posi+1] , list_index , posi+1))
        
    return final_list