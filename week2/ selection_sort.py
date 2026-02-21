def selection_sort(L : list) -> list:
    
   
    l = 0
    r = len(L)
    while(l < len(L) - 1):
        min = l
        for i in range(l , r):
            if(L[i] < L[min]):
                min = i
                
        temp = L[min]
        L[min] = L[l]
        L[l] = temp 
        
        l+=1
        
    return L 


print(selection_sort([5,4,3,2,1,0]))
        
         
        