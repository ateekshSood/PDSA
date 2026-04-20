class min_heap:
    
    def __init__(self):
        self.arr = []
        
    def heapify_up(self):
        i = len(self.arr) - 1
        while i>0:
            p = (i-1)//2
            
            if self.arr[i] < self.arr[p]:
                (self.arr[i] , self.arr[p]) = (self.arr[p] , self.arr[i])
                i = p
            else:
                break 
            
    def insert(self , value):
        self.arr.append(value)
        self.heapify_up()
        
    def heapify_down(self , i):
        n = len(self.arr)
        while i<n:
            
            smallest = i
            left_child = 2*i + 1
            right_child = 2*i + 2
            
            if left_child<n and self.arr[left_child] < self.arr[smallest]:
                smallest = left_child
                
            if right_child < n and self.arr[right_child] < self.arr[smallest]:
                smallest = right_child 
                
            if smallest != i:
                self.arr[i] , self.arr[smallest] = self.arr[smallest] , self.arr[i]
                i = smallest 
            else:
                break 
                
    def build(self , lst):
        self.arr = lst[:]
        n = len(self.arr)
        
        for i in range(n // 2 -1 , -1 , -1):
            self.heapify_down(i)
        
        
    def delete_min(self):
        min = self.arr[0]
        self.arr[0] = self.arr.pop()
        self.heapify_down(0)
        return min
        