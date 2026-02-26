def insertion_sort(L : list) -> list:
    
    for i in range(len(L)):
        
        j = i 
        while( j > 0 and L[j] < L[j-1]):
            (L[j] , L[j-1]) = (L[j-1] , L[j])
            j = j-1 
            
    
    return L 

print(insertion_sort([4,3,2,1]))