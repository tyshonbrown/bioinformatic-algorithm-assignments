# pick two points closest to eachother, points with the lowest value in the distance matrix
def argmin(matrix, n):
    # minimun distance is init to infinity
    min_distance = float('inf')
    closest_pair = (None, None)
    
    for i in range(n):
        for j in range(i + 1, n):
            
            # minimum distance and pair updated
            if matrix[i][j] < min_distance:
                min_distance = matrix[i][j]
                closest_pair = (i, j)
    
    return closest_pair, min_distance

# compute the average distance between two clusters
def cluster_distance(cluster1, cluster2, matrix):
    
    # looks at value in original matric
    distances = [
        matrix[i][j]
        for i in cluster1
        for j in cluster2
        if i != j
    ]
    
    # returns the average distance
    return sum(distances) / len(distances) if distances else 0.0

# clustering algorithm using average linkage
def compute(original_matrix, n):
    
    # this matrix will be updated while original stays the same
    matrix = original_matrix
    
    # individual clusters, looks like [[0], [1], ..., [n - 1]]
    clusters = [[i] for i in range(n)]
    
    # keep track of the order in which clusters are created
    order = []
    
    # while we have more than one cluster
    while len(clusters) > 1:
        
        # select the points closest to each other
        (i, j), min_distance = argmin(matrix, len(matrix))
        
        # combine clusters
        new_cluster = clusters[i] + clusters[j]
        
        # removing the original clusters, preserving order
        clusters.pop(max(i, j))
        clusters.pop(min(i, j))
        
        # adding the new cluster
        clusters.append(new_cluster)
        order.append(new_cluster)
        
        # recompute the distance matrix
        new_matrix = []
        for x in range(len(clusters)):
            row = []
            for y in range(len(clusters)):
                if x == y:
                    row.append(0.0)
                
                else:
                    # calculate the distance and add it to the row
                    average_dist = cluster_distance(clusters[x], clusters[y], original_matrix)
                    row.append(average_dist)
            
            # adding each row to the updated matrix    
            new_matrix.append(row)
            
        matrix = new_matrix
    
    # since the points are 0-index in the clusters, they are updated to be 1-index
    for lst in order:
        for i in range(len(lst)):
            lst[i] += 1
            
    return order

if __name__ == "__main__":
    
    with open("input", "r") as file:
        n = int(file.readline().strip())
        matrix = []
        for _ in range(n):
            row = list(map(float, file.readline().strip().split()))
            matrix.append(row)
    
    result = compute(matrix, n)
    #print(result)
    
    with open("output", "w") as file:
        for i, cluster in enumerate(result):
            line = ' '.join(str(x) for x in cluster)
            
            if i < len(result) - 1:
                file.write(line + '\n')
                
            else:
                file.write(line) 
    
    