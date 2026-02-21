#simple normal binary search 

def binarySearch(L : list , k : int) -> bool:
    
    left = 0
    right = len(L) - 1
    
    while(left <= right):
        mid = (left + right)//2
        
        if(L[mid] == k):
            return True
        
        elif (L[mid] > k):
            right = mid - 1
            
        else:
            left = mid+1
    
    return False

print(binarySearch([1,2,3,4,5] , -3))