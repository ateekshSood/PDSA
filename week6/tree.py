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
    
    def inorder(self):
        
        if self.isEmpty():
            return ([])
        
        else:
            return self.left.inorder() + [self.value] + self.right.inorder()
        
    def postorder(self):
        
        if self.isEmpty():
            return []
        
        else:
            return self.left.postorder() + self.right.postorder() + [self.value]
        
        
    def find(self , v):
        
        if(self.isEmpty()):
            return False
        
        if(self.value == v):
            return True
        
        elif(self.value > v):
            self.left.find(v)
            
        elif(self.value < v):
            self.right.find(v)
            
    def findMax(self):
        
        if(self.right.isEmpty()):
            return self.value
        
        else:
            return(self.right.findMax())
    
    def findMin(self):
        
        if(self.left.isEmpty()):
            return self.value 
        
        else:
            return (self.left.findMin())
        
        
    def insert(self , v):
        if self.isEmpty():
            self.value = v
            self.left = Tree()
            self.right = Tree() 
        
        elif self.value > v:
            self.left.insert(v)
        
        elif self.value < v:
            self.right.insert(v)
            
        else:
            return
        
    def makeempty(self):
        self.value = None 
        self.left = None 
        self.right = None 
        
        return 
    
    def copyleft(self):
        
        self.value = self.left.value
        self.left = self.left.left 
        self.right = self.left.right
        
        return 
    
    def copyright(self):
        
        self.value = self.right.value 
        self.left = self.right.left 
        self.right = self.right.right 
    
    
    def delete(self , v):
        
        
        if(self.isEmpty()):
            return 
        
        elif v > self.value:
            self.right.delete(v)
            
        elif v < self.value:
            self.left.delete(v)
            
        elif v == self.value:
            
            if self.isleaf():
                self.makeempty()
                
            elif self.left.isEmpty():
                self.copyright()
                
            elif self.right.isEmpty():
                self.copyleft()
                
            else:
                self.value = self.left.findMax()
                self.left.delte(self.left.findMax())
                
            return 

    def __str__(self):
        return str(self.postorder())
    
    
def main():
    tree = Tree()
    tree.insert(10)
    tree.insert(30)
    tree.insert(20)
    tree.insert(40)
    tree.insert(50)
    
    print(tree)
    
    
    
    
if (__name__ == "__main__"):
    main()
    
    