
def read_maze(file_name):
    try:
        with open(file_name) as fh:
            maze = [[char for char in line.strip("\n")] for line in fh]
            num_cols_top_row = len(maze[0])
            for row in maze:
                if len(row) != num_cols_top_row:
                    print("the maze is not rectangular")
                    raise SystemExit
            return maze
    except OSError:
        print("There is a problem with the file you have selected")
        raise SystemExit


if __name__ == "__main__":
    maze = read_maze("mazes/challenge_maze.txt")
    for row in maze:
        print(row)