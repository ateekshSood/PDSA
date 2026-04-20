import numpy as np

#O(n**2) with adjacency matrix


def dijkstra(A_Matrix , s):
    
    (rows , columns , x) = A_Matrix.shape
    inf = np.float('inf')
    (visited , distance) = ({} , {})
    
    distance[s] = 0
    
    for v in range(rows):
        (visited[v] , distance[v]) = (False , inf)
        
    for u in range(rows):
        
        nextdistance = min(distance[v] for v in range(rows) if not visited[v])
        nextvlist = [ v for v in range(rows) if not visited[v] and distance[v] == nextdistance]   
        
        if (next == []):
            break
        
        nextv = min(nextvlist)
        visited[nextv]  = True 
        
        for v in range(columns):
            if A_Matrix[nextv , v , 0] == 1 and not visited[v] :
                distance[v] = min(distance[v] , distance[nextv] + A_Matrix[nextv , v , 1])
        
         
    return distance
    
#with adjacency list 
def dijkstra(A_List , s):
    
    inf = np.float('inf')
    (visited , distance) = ({} , {})
    
    for v in A_List.keys():
        (visited[v] , distance[v]) = (False , inf)
        
    distance[s] = 0
    
    for v in A_List.keys():
        
        next_d = min(distance[v] for v in A_List.keys() if not visited[v])
        
        next_v = [v for v in A_List.keys() if not visited[v] and distance[v] == next_d]
        
        if next_v == []:
            break
        
        chosen_v = min(next_v)
        visited[chosen_v] = True
        
        for (v,d) in A_List[chosen_v]:
            distance[v] = min(distance[v] , distance[chosen_v] + d)
    
    return distance
    
