import sys
sys.setrecursionlimit(2000)  # Set a new limit


# Does an initial check whether the maze is solvable or not
def initialMazeCheck(maze, start_point, goal):
    # Checks if start and goal points are clear
    if (maze[0][1] == 0 or maze[1][0] == 0) and (maze[-2][-1] == 0 or maze[-1][-2] == 0) and maze[start_point[0]][start_point[1]] == 0 and maze[goal[0]][goal[1]] == 0:
        return True  # Path is clear

    # Checks for blockage at the start point
    if maze[0][1] == 1 and maze[1][0] == 1:
        print("Start point is being blocked")
        return False  # Start point blocked

    # Checks for blockage at the goal point
    elif maze[-2][-1] == 1 and maze[-1][-2] == 1:
        print("Goal point is being blocked")
        return False  # Goal point blocked

    return None  # Returns None if no conditions are met
