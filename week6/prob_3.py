class max_heap:
    
    def __init__(self):
        self.arr = []
        
    def heapify_up(self):
        
        i = len(self.arr) - 1 
        
        while i > 0 : 
            
            p = (i - 1)//2 
            
            if self.arr[i] > self.arr[p]:
                (self.arr[i] , self.arr[p]) = (self.arr[p] , self.arr[i])
                i = p 
            else:
                break
                
        
    def insert(self , value):
        self.arr.append(value)
        self.heapify_up()
        
    def heapify_down(self , index):
        
        i = index 
        n = len(self.arr)
        
        while i < n:
            
            largest = i
            left_child = 2 * i + 1 
            right_child = 2 * i + 2 
            
            if left_child < n and self.arr[left_child] > self.arr[largest]:
                largest = left_child
                
            if right_child < n and self.arr[right_child] > self.arr[largest]:        
                largest = right_child 
                
            if largest != i:
                
                (self.arr[i] , self.arr[largest]) = (self.arr[largest] , self.arr[i])
                i = largest
                
            else:
                break 
            
    def get_arr(self):
        return self.arr
    
def min_max(arr):
    
    heap = max_heap()
    
    for element in arr:
        heap.insert(element)
        
    return heap.get_arr()   
    
    
