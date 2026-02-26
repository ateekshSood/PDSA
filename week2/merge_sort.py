import time as t

def merge(left_list : list , right_list : list):
    left_len = len(left_list)
    right_len = len(right_list)
    l , r = 0 , 0

    merged_list = []
    
    while(l < left_len and r < right_len):
        
        if(left_list[l] <= right_list[r]):
            merged_list.append(left_list[l])
            l +=1
            
        else:
            merged_list.append(right_list[r])
            r+=1
            
    merged_list.extend(left_list[l:])
    merged_list.extend(right_list[r:])
    
    return merged_list
        

def merge_sort(L : list) -> list:
    
    if(len(L)<=1):
        return L
    
    mid = len(L)//2
    
    left_list = merge_sort(L[:mid])
    right_list = merge_sort(L[mid:])
        
    return merge(left_list , right_list)

start = t.time()
print(merge_sort(['d2' , 'd1' , 'b3' , 'a4']))
end = t.time()
print(f"time taken: {(end - start):.4f}" )
 
print('a2' > 'a1')