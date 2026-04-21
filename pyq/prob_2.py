def closest_pair_min_difference(L):
    
    L.sort()
    
    min_diff = float('inf')
    
    for i in range(1 , len(L)):
        
        min_diff = min(min_diff , abs(L[i] - L[i-1]))
        
    return min_diff
    