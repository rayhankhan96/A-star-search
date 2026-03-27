import heapq

# Manhattan Distance
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* Algorithm
def astar(grid, start, goal, R, C):
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    open_list = []
    heapq.heappush(open_list, (0, start))
    
    came_from = {}
    g_cost = {start: 0}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, g_cost[goal]

        for d in directions:
            neighbor = (current[0] + d[0], current[1] + d[1])

            if 0 <= neighbor[0] < R and 0 <= neighbor[1] < C:
                if grid[neighbor[0]][neighbor[1]] == 1:
                    continue

                new_cost = g_cost[current] + 1

                if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                    g_cost[neighbor] = new_cost
                    priority = new_cost + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (priority, neighbor))
                    came_from[neighbor] = current

    return None, None


# 🔹 Read from input1.txt
with open("input1.txt", "r") as f:
    data = f.read().strip().splitlines()

R, C = map(int, data[0].split())

grid = []
for i in range(1, R+1):
    grid.append(list(map(int, data[i].split())))

sr, sc = map(int, data[R+1].split())
tr, tc = map(int, data[R+2].split())

start = (sr, sc)
goal = (tr, tc)

# Run A*
path, cost = astar(grid, start, goal, R, C)

# Output
if path:
    print(f"Path found with cost {cost} using A*")
    print("Shortest Path:", path)
else:
    print("Path not found using A*")