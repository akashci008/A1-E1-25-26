def tsp_nearest_neighbor(cost):
    n = len(cost)
    
    visited = [False] * n
    current = 0
    visited[current] = True
    
    path = [current]
    total_cost = 0

    for _ in range(n - 1):
        nearest = -1
        min_dist = float('inf')

        for i in range(n):
            if not visited[i] and cost[current][i] < min_dist:
                min_dist = cost[current][i]
                nearest = i

        visited[nearest] = True
        path.append(nearest)
        total_cost += min_dist
        current = nearest

 
    total_cost += cost[current][0]
    path.append(0)

    return path, total_cost



n = int(input("Enter number of cities: "))

print("Enter cost matrix:")
cost = []
for i in range(n):
    row = list(map(int, input().split()))
    cost.append(row)

path, total_cost = tsp_nearest_neighbor(cost)

print("Path:", " -> ".join(map(str, path)))
print("Total Cost:", total_cost)
