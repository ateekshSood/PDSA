def mergeAndCount(L : list[int], R : list[int]):
    
    (left_len , right_len) = (len(L) , len(R))
    (combined , i , j , k , count) = ([] , 0 , 0 , 0  ,0)
    
    while k<(left_len + right_len):
        
        if i == left_len:
            combined.append(R[j])
            (k , j) = (k+1 , j+1)
            
        elif j == right_len:
            combined.append(L[i])
            (k , i) = (k+1 , i+1)
            
        elif L[i] < R[j]:
            combined.append(L[i])
            (i , k) = (i+1 , k+1)
            
        else:
            combined.append(R[j])
            (j , k , count) = (j+1 , k+1 , count+(left_len - i))
            
    return (combined , count)


def sortAndCount(l : list):
    
    n = len(l)
    
    if n<= 1:
        return (l , 0)
    
    (l , countl) = sortAndCount(l[:n//2])
    (r , countr) = sortAndCount(l[n//2:])
    
    (comb , countcomb) = mergeAndCount(l , r)
    
    return (comb , countcomb + countl + countr)