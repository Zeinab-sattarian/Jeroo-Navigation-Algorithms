Jeroo Navigation Algorithms
Introduction

This repository contains two Python scripts that simulate a Jeroo navigating a grid. The Jeroo must perform tasks such as picking up a flower, planting it at another location, and then moving to a final position. The first script uses the A* algorithm for pathfinding, while the second script employs the Breadth-First Search (BFS) algorithm.

Prerequisites
Python 3.x
heapq module (standard library)
collections module (standard library)
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your_username/jeroo-navigation.git
cd jeroo-navigation
Usage
Script 1: A* Algorithm
This script demonstrates pathfinding using the A* algorithm on a 10x10 grid with random walls.

Running the Script
bash
Copy code
python a_star_jeroo.py
Code Overview
Grid Initialization:

A 10x10 grid is generated with random walls (1 represents a wall, 0 represents an open cell).
Random positions for the start, flower, plant, and final locations are chosen.
A Pathfinding*:

The heuristic function calculates the Manhattan distance.
The a_star function finds the shortest path from the start to the goal.
Jeroo Movement:

The move_jeroo function finds and prints the paths for the Jeroo to pick the flower, plant it, and move to the final position.
Script 2: Breadth-First Search (BFS) Algorithm
This script demonstrates pathfinding using the BFS algorithm on a 4x4 grid.

Running the Script
bash
Copy code
python bfs_jeroo.py
Code Overview
Grid Initialization:

A 4x4 grid is initialized.
Fixed positions for the start, flower, plant, and final locations.
BFS Pathfinding:

The bfs function finds the shortest path from the start to the goal.
Jeroo Movement:

The move_jeroo function finds and prints the paths for the Jeroo to pick the flower, plant it, and move to the final position.
Grid Visualization
The grid is visualized in the console:

# represents a wall.
. represents an open cell.
Example Output for A* Algorithm:

makefile
Copy code
Grid:
..........
.#....#...
.#.#......
.....#....
..#.......
....#.....
.#..#.....
...#......
.#..#.....
..........
Move to (0, 1)
Move to (0, 2)
...
Pick flower at (5, 6)
Move to (5, 7)
Move to (5, 8)
...
Plant flower at (8, 9)
Move to (8, 8)
Move to (8, 7)
...


Acknowledgments
Developed by Zeinab Sattarian
