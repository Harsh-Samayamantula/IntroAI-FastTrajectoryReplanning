from prettytable import PrettyTable
import random
class GridWorld:
    def __init__(self, columns, rows):
        self.cols = columns
        self.rows = rows
        self.valid_grid_world = False
        # self.white = 0
        # self.black = 0

    def make_grid(self):
        self.grid = []
        for row in range (0, self.rows):
            row_arr = []
            for col in range (0, self.cols):
                # row_arr.append('⬜' if random.random() < 0.7 else '⬛')
                row_arr.append(' ' if random.random() < 0.7 else 'X')
            self.grid.append(row_arr)

    def is_valid_grid_world(self):
        visited_arr = [[False for col in range(self.cols)] for row in range(self.rows)] 
        # self.dfs_recursive(self.grid, 0, 0, visited_arr)
        self.dfs_iterative(self.grid, 0, 0, visited_arr)
        print(f'THIS GRID IS {"VALID" if self.valid_grid_world else "INVALID"}')
        return self.valid_grid_world
    
    # Is throwing Maximum recursion depth reached error!
    def dfs_recursive(self, grid, row, col, visited):
        # Check if row or col are out of bounds
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols or self.valid_grid_world:
            return
        # Check if the current cell is a wall or has been visited
        if grid[row][col] == 'X' or visited[row][col]:
            return
        # Check if the current cell is the destination
        if row == len(grid) - 1 and col == len(grid[0]) - 1:
            print("Destination reached!")
            self.valid_grid_world = True
            return
    
        # Mark current cell as visited
        visited[row][col] = True
        print(f"Visiting cell: ({row}, {col})")
    
        # Explore neighbors in a specific order: up, right, down, left
        
        self.dfs(grid, row - 1, col, visited)  # Up
        self.dfs(grid, row, col + 1, visited)  # Right
        self.dfs(grid, row + 1, col, visited)  # Down
        self.dfs(grid, row, col - 1, visited)  # Left
    
    def dfs_iterative(self, grid, start_row, start_col, visited):
        stack = []
        stack.append((start_row, start_col))
        
        while stack:
            row, col = stack.pop()
            # Checking if out of bounds or Wall or already visited
            if row < 0 or row >= self.rows or col < 0 or col >= self.cols or grid[row][col] == 'X' or visited[row][col]:
                continue
            # Checking to see if goal is reached
            if row == self.rows - 1 and col == self.cols - 1:
                print("Destination reached!")
                self.valid_grid_world = True
                return
            # Marking Visited
            visited[row][col] = True
            print(f"Visiting cell: ({row}, {col})")
            # Push unvisited neighbors onto the stack: up, right, down, left
            stack.append((row - 1, col))  # Up
            stack.append((row, col + 1))  # Right
            stack.append((row + 1, col))  # Down
            stack.append((row, col - 1))  # Left

    def print_grid(self):
        # print(self.grid)
        x = PrettyTable()
        x.field_names = [f'{i}' for i in range(0, self.cols)]
        x.add_rows(self.grid)
        print(x)
        # print(self.white, self.black)
