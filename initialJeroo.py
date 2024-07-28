from collections import deque
#-----------------------------------Zeinab Sattarian 

# Define the grid dimensions and positions
n, m = 4, 4  # Example grid size (4x4)
start_pos = (0, 0)
flower_pos = (3, 0)
plant_pos = (3, 2)
final_pos = (4, 2)

# Direction vectors for moving in the grid (East, West, North, South)
directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

# Initialize the grid
grid = [[0 for _ in range(m)] for _ in range(n)]
grid[flower_pos[0]][flower_pos[1]] = 1  # Flower location

# BFS implementation to find the shortest path to the flower
def bfs(start, target):
    queue = deque([start])
    visited = set([start])
    parent = {start: None}

    while queue:
        current = queue.popleft()

        if current == target:
            break

        for d in directions:
            neighbor = (current[0] + d[0], current[1] + d[1])

            if 0 <= neighbor[0] < n and 0 <= neighbor[1] < m and neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = current

    # Reconstruct the path
    path = []
    step = target
    while step is not None:
        path.append(step)
        step = parent[step]
    path.reverse()
    return path

# Simulate jeroo actions based on the path
def move_jeroo():
    path_to_flower = bfs(start_pos, flower_pos)
    for step in path_to_flower[1:]:  # Skip the start position
        print(f"Move to {step}")

    print("Pick flower at", flower_pos)

    path_to_plant = bfs(flower_pos, plant_pos)
    for step in path_to_plant[1:]:  # Skip the flower position
        print(f"Move to {step}")

    print("Plant flower at", plant_pos)

    # Final step to the target after planting
    final_step = (plant_pos[0], plant_pos[1] + 1)
    print(f"Move to {final_step}")

move_jeroo()
