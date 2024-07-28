import heapq

#-----------------------------------Zeinab Sattarian


# Define the grid dimensions
n, m = 10, 10  # Example grid size (10x10)

# Define the grid with random walls, 0 is an open cell, 1 is a wall
import random
grid = [[0 if random.random() > 0.2 else 1 for _ in range(m)] for _ in range(n)]

# Define positions
start_pos = (0, 0)
flower_pos = (random.randint(0, n-1), random.randint(0, m-1))
plant_pos = (random.randint(0, n-1), random.randint(0, m-1))
final_pos = (random.randint(0, n-1), random.randint(0, m-1))

# Make sure positions are not walls
grid[flower_pos[0]][flower_pos[1]] = 0
grid[plant_pos[0]][plant_pos[1]] = 0
grid[final_pos[0]][final_pos[1]] = 0

# Print grid for visualization
print("Grid:")
for row in grid:
    print("".join(['#' if cell == 1 else '.' for cell in row]))

# Direction vectors for moving in the grid (East, West, North, South)
directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def heuristic(a, b):
    """Heuristic function for A* (Manhattan distance)"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(start, goal):
    """A* algorithm to find the shortest path"""
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start))
    came_from = {}
    g_score = {start: 0}
    
    while open_set:
        _, current_cost, current = heapq.heappop(open_set)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        for d in directions:
            neighbor = (current[0] + d[0], current[1] + d[1])
            
            if 0 <= neighbor[0] < n and 0 <= neighbor[1] < m and grid[neighbor[0]][neighbor[1]] == 0:
                tentative_g_score = current_cost + 1
                
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score, tentative_g_score, neighbor))
                    came_from[neighbor] = current
                    
    return []

def move_jeroo():
    path_to_flower = a_star(start_pos, flower_pos)
    if not path_to_flower:
        print("No path to flower.")
        return
    
    for step in path_to_flower[1:]:
        print(f"Move to {step}")
    print("Pick flower at", flower_pos)

    path_to_plant = a_star(flower_pos, plant_pos)
    if not path_to_plant:
        print("No path to plant.")
        return
    
    for step in path_to_plant[1:]:
        print(f"Move to {step}")
    print("Plant flower at", plant_pos)

    path_to_final = a_star(plant_pos, final_pos)
    if not path_to_final:
        print("No path to final position.")
        return
    
    for step in path_to_final[1:]:
        print(f"Move to {step}")

move_jeroo()
