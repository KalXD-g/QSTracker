import random
import sys
sys.setrecursionlimit(2000)  # Set a new limit


# Generates a random maze. This function is AI generated.
def generate_maze(width, height, obstacle_percentage):
    # Create a maze filled with zeros (paths)
    maze = [[0 for _ in range(width)] for _ in range(height)]

    # Set start and end points
    start_point = (0, 0)
    end_point = (height - 1, width - 1)

    # Randomly place obstacles based on the specified percentage
    total_cells = width * height
    num_obstacles = int(total_cells * (obstacle_percentage / 100))

    # Ensure that the start and end points are not blocked
    while num_obstacles > 0:
        x = random.randint(0, height - 1)
        y = random.randint(0, width - 1)
        if (x, y) != start_point and (x, y) != end_point and maze[x][y] == 0:
            maze[x][y] = 1  # Place an obstacle
            num_obstacles -= 1

    # Ensure the maze is solvable by removing obstacles along a path
    # Create a simple path from start to end
    current_position = start_point
    while current_position != end_point:
        maze[current_position[0]][current_position[1]] = 0  # Clear the path
        if current_position[0] < end_point[0]:
            current_position = (
                current_position[0] + 1, current_position[1])  # Move down
        elif current_position[1] < end_point[1]:
            current_position = (
                current_position[0], current_position[1] + 1)  # Move right

            return maze