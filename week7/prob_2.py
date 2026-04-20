def minimum_platform(train_schedule):
    arrival_time = sorted(int(train[1].replace(":" , "")) for train in train_schedule)
    departure_time = sorted(int(train[2].replace(":" ,"")) for train in train_schedule)
    
    (i , j) = (0 , 0)
    
    n = len(train_schedule)
    max_platform = 0 
    platform_needed = 0 
    
    while i < n and j < n:
        
        if arrival_time[i] <= departure_time[j]:
            platform_needed+=1 
            i+=1 
            
        else:
            platform_needed-=1 
            j+=1 
            
        if platform_needed >= max_platform:
            max_platform = platform_needed
            
    return max_platform