class Tree:
    
    def __init__(self , initial_value = None):
        self.value = initial_value
        
        if self.value:
            self.left = Tree()
            self.right = Tree()
            
        else:
            self.left = None
            self.right = None 
            
        return 
    
    def isEmpty(self):
        return (self.value == None)
    
    def isleaf(self):
        return (self.value != None and self.left.isEmpty()  and self.right.isEmpty() )
    
    