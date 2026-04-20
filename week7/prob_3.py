def no_overlap(L):
    
    L.sort(key = lambda x : x[2])
    final_list = []
    end_day = 0 
    start_day = 0
    
    for i in range(len(L)):
        
        if i == 0:
            final_list.append(L[i])
            end_day = L[i][2]
            
        start_day = L[i][1]
        
        if start_day > end_day:
            final_list.append(L[i])
            end_day = L[i][2]
            
    return [i[0] for i in final_list]
            
        