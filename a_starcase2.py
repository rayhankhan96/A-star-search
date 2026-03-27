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
            nr, nc = current[0] + d[0], current[1] + d[1]

            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 0:
                neighbor = (nr, nc)
                temp_g = g_cost[current] + 1
                if neighbor not in g_cost or temp_g < g_cost[neighbor]:
                    g_cost[neighbor] = temp_g
                    f_cost = temp_g + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_cost, neighbor))
                    came_from[neighbor] = current

    return None, None


# 🔹 Read from input2.txt (VS Code)
with open("input2.txt", "r") as f:
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