#find missing element in the sorted list 

def missing_number(L):
    
    l = 0 
    r = len(L) -1 
    
    while ( l <= r):
        
        mid = (l+r)//2 
        
        if L[0] != 1 :
            return 1
        
        if mid > 0:
            
            if L[mid-1] + 1 != L[mid]:
                return L[mid] - 1 
            
            elif L[mid+1] - 1  != L[mid]:
                return L[mid] + 1
        
        elif(mid - l < L[mid] - L[l] ):
            r = mid - 1 
            
        elif (r - mid < L[r] - L[mid] ):
            l = mid + 1
            
               
            
print(missing_number([2,3,4,5]))

# array 1 to n 