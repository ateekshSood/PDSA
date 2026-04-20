def maxLessThan(root , k):
    max = None 
    temp = root 
    
    while not temp.isempty():
        
        if temp.value ==  k:
            
            return temp.value
                
        elif temp.value < k:
            
            max = temp.value
            temp = temp.right
            
        else:
            temp = temp.left 
             
                
    return max
                
        
