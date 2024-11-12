import sys
sys.setrecursionlimit(2000)  # Set a new limit




# Creates a tracker
def tracker(maze, position,goal):
    x, y = position

    # checks if the position is valid
    if x < 0 or y < 0 or x >= len(maze) or y >= len(maze[0]) or maze[x][y] != 0:
        return None

    maze[x][y] = 2  # Marks as visited

    if position == goal:
        print("Goal reached")
        return True  # Goal reached

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up
    valid_moves = []  # to store valid next moves

    for direction in directions:
        new_position = (x + direction[0], y + direction[1])

        # Checks if the next point is valid and not already visited
        if (0 <= new_position[0] < len(maze) and 0 <= new_position[1] < len(maze[0]) and maze[new_position[0]][new_position[1]] == 0):
            valid_moves.append(new_position)  # collects all the valid moves

    for next_position in valid_moves:
        if tracker(maze, next_position, goal):  # New tracker for each valid path
            return True

    return False  # Return False if no paths lead to the goal
