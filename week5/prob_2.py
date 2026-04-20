def make_path(path , D):
  
    final_path = [D]
    iterator = D
    while path[iterator] is not None:
        
        final_path.append(path[iterator])
        iterator = path[iterator]
        

    final_path.reverse()
    return final_path



def dijkstra(WList , S , D):
    
    distance = {key : float('inf') for key in WList.keys()}
    visited = {key : False for key in WList.keys()}
    path = {key : None for key in WList.keys()}
    distance[S] = 0 
    
    for key in WList.keys():
        
        min_distance = min(distance[v] for v in WList.keys() if not visited[v])
        next_vertex_list = [v for v in WList.keys() if not visited[v] and distance[v] == min_distance]
        
        if next_vertex_list == []:
            return []
        
        next_v = min(next_vertex_list)
        visited[next_v] = True 
        
        for k in WList[next_v]:
            
            if not visited[k[0]]:

                if distance[k[0]] > distance[next_v] + k[1]:
                    distance[k[0]] = distance[next_v] + k[1]
                    path[k[0]] = next_v 
    
    return distance[D] , make_path(path , D)

def min_cost_walk(WList , S , D , V):
    
    distance_S_to_V , path_S_to_V = dijkstra(WList , S , V)
    distance_V_to_D , path_v_to_D = dijkstra(WList , V , D)
    
    final_path = path_S_to_V + path_v_to_D[1:]
    
    return ( (distance_S_to_V + distance_V_to_D) , final_path)