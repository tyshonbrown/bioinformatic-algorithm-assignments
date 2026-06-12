import random, math

def euclidean_distance(points1, points2):
    
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(points1, points2)))

def calculate_center(cluster):
    if not cluster:
        return []
    
    n = len(cluster[0])
    center = [0.0] * n
    
    for point in cluster:
        for i in range(n):
            center[i] += point[i]
            
    return [x / len(cluster) for x in center]

def loyds_algorithm(data, k):
    
    centers = data[:k]

    while True:
        clusters = [[] for _ in range(k)]
        
        for point in data:
            distances = [euclidean_distance(point, center) for center in centers]
            cluster_index = distances.index(min(distances))
            clusters[cluster_index].append(point)
    
        new_centers = [calculate_center(cluster) for cluster in clusters]
        
        if new_centers == centers:
            break
        centers = new_centers
        
    return centers

if __name__ == "__main__":
    
    with open("input", "r") as f:
        header = f.readline().strip()
        k, n = map(int, header.split())
        
        points = []
        for line in f:
            coordinates = list(map(float, line.strip().split()))
            points.append(coordinates)
        
    result = loyds_algorithm(points, k)
    
    with open("output", "w") as f:
        
        for i, center in enumerate(result):
            line = ' '.join(map(str, center))
            f.write(line + ('\n' if i < len(result) - 1 else ''))