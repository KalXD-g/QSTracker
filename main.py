import time
import sys
sys.setrecursionlimit(2000)  # Set a new limit

from mazgen import *
from initcheck import *
from tracker import *


# Set parameters
width, height = 100, 100
obstacle_percentage = 30  # Adjust this percentage for more or fewer obstacles

# Generate the maze
maze = generate_maze(width, height, obstacle_percentage)

# Print the maze in 2D matrix format
for row in maze:
    print(row)

start_point = (0, 0)
goal = (49, 49)

if initialMazeCheck(maze, start_point, goal):
    start_time = time.time()
    tracker(maze, start_point, goal)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken to solve the maze: {elapsed_time:.4f} seconds")
else:
    print("The maze cannot be traversed from the start to the goal.")
