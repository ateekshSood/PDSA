class Node:
    def __init__(self , data):
        self.data = data 


def insert_at_end(data , head):
    
    new_node = Node(data)
    
    if head == None:
        head = new_node
    
    else:
        
        temp = head
        while temp.next != None:
            temp = temp.next 
            
    
        temp.next = new_node 
        new_node.next = None 
    
    