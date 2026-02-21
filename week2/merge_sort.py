def merge(left_list : list , right_list : list):
    left_size = len(left_list) 
    right_size = len(right_list)
    left_pointer = 0
    right_pointer = 0
    
    while(left_pointer < left_list or right_pointer < right_size):
        
        if(left_list[left_pointer] >= right_list[right_pointer]):
            temp = right_list[right_pointer]
            right_list[right_pointer] = left_list[left_pointer]
            left_list[left_pointer] = temp
            
        
                   
    
    

def merge_sort(L : list , left , right) -> list:
    mid = (left + right)//2
    
    merge_sort(L[left: mid-1] , left , mid-1)
    merge_sort(L[mid+1 : right +1] , mid+1 , right)
    merge(L[left : mid-1] , L[mid+1 , right+1])
