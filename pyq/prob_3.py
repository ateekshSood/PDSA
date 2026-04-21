#kruskal 

def krushkal(adj_list):
    
    (TE , components , edges , min_cost) = ([] , {} , [] , 0)
    
    for u in adj_list.keys():
        
        edges.extend([(d , u , v) for (v , d) in adj_list[u]])
        components[u] = u 
        
    edges.sort()
    
    for (d , u , v) in edges:
        
        if components[u] != components[v]:
            TE.append((u,v))
            min_cost+=d 
        
            
            for c in components.keys():
                if c != u and components[c] == components[u]:
                    components[c] = components[v]
                    
            components[u] = components[v]
                    
    return min_cost


def build_road(cost_list):
    
    return krushkal(cost_list)
         
