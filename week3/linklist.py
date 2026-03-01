class Node:
    def __init__(self , val : int):
        self.data = val 
        self.next = None



class LinkedList:
    
    def __init__(self , head_value : int):
        self.head = Node(head_value)
        
        
    def addVal(self , data ,  index):
        if not self.head:
            raise ValueError("Please init head first")
        
        else:
            newNode = Node(data)
            temp = self.head 
            
        
            if(index == 0):
               newNode.next = self.head
               self.head = newNode
    
    
            else:

                i=0
                while(i<index-1 and temp.next is not None):
             
                    temp = temp.next
                    i+=1
                
                newNode.next = temp.next 
                temp.next = newNode 

            
    def removeVal(self , index):
        if not self.head:
            raise ValueError("Please init head first")
        
        
            
            
    def display(self):
        temp = self.head 
        while(temp != None):
            print(f"{temp.data} -> " ,end="")
            temp = temp.next 
            
        print("None")
        
        
    def reverse(self):
        if self.head == None:
            return
        temp0 = None 
        temp1 = self.head 
        temp2 = temp1.next 
        
        while(temp2 is not None):
            temp1.next = temp0 
            temp0 = temp1
            temp1 = temp2 
            temp2 = temp2.next 
        
        temp1.next = temp0 
        self.head = temp1 
        
         
            
        

ll = LinkedList(1)


for index , i in enumerate(range(1,5)):
    ll.addVal(i , index)
ll.display()