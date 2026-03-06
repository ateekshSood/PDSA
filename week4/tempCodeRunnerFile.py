import numpy as np 

rng = np.random.default_rng(42)
x1 = (rng.random((9)) * 2).round(0).astype(np.int32)
x2 = (rng.random((9)) * 2).round(0).astype(np.int32)

points = np.column_stack((x1, x2))
adjacency_matrix = np.zeros((3,3))
print(points)

for i in range(points.shape[0]):
    i , j = points[i , 0] , points[i , 0]
    adjacency_matrix[i , j] = 1
    
print(adjacency_matrix)
