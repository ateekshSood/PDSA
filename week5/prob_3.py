def bellman_ford(WList, s):
    
    distance = {v : float('inf') for v in WList.keys()}
    distance[s] = 0
    
    for _ in range(len(WList.keys()) - 1):
        
        for v in WList.keys():
           for (u,d) in WList[v]:
                
                    distance[u] = min(distance[u] , distance[v] + d)
               
                    
    is_negative_cycle = False
                
    for _ in range(len(WList.keys()) - 1):
    
        for v in WList.keys():
            
            for (u,d) in WList[v]:
                
                if distance[u] > distance[v] + d:
                    return True 
                    
    return is_negative_cycle


def isNegativeWeightCyclePresent(WList):
    return bellman_ford(WList , 0 )