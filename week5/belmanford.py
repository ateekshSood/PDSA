import numpy as np

def bellmanford(A_Mat , s):
    (rows , cols , x) = A_Mat.shape
    inf = np.inf
    distance= {}
    
    for v in range(rows):
        distance[v] = inf
        
    distance[s] = 0
    
    for i in range(rows - 1):
        for u in range(rows):
            for v in range(cols):
                
                if(A_Mat[u , v , 0] == 1):
                    distance[v] = min(distance[v] , distance[u] + A_Mat[u , v , 1])
                    
    
    return distance

nums=[1,2,3,4,5]
prefix_array = []

for i in range(len(nums)):
    if i == 0:
        prefix_array.append(nums[i])
    else:
        prefix_array.append(prefix_array[i-1] + nums[i])  
        
        
print(prefix_array)
