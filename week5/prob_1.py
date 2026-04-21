def krushkal(distance_map):
    (edges , components , TE) = ([] , {} , [])
    
    for u in distance_map.keys():
        edges.extend((d , u , v) for (v ,  d) in distance_map[u])
        components[u] = u 
        
    edges.sort()
     
    for (d , u , v) in edges: 
        if components[u] != components[v]:
            TE.append((u,v))

            old_component = components[u]
            for x in distance_map.keys():
                if components[x] == old_component:
                    components[x] = components[v]
                    
    return TE 

def FiberLink(distance_map):
    
    TE = krushkal(distance_map)
    distance = 0 
    for (u , v) in TE:
        
        for edge in distance_map[u]:
            
            if edge[0] == v:
                distance += edge[1]
                
    return distance
    
    