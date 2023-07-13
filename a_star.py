#Hueristic Function
#h-val = undefined
#--> manhattan distance from current coordinate to goal (bottom-right corner)
# |(100-x)|+|(100-y)| = h value

#Start w g value = infinity
#Increment g value as you keep moving through the world (+1 every time you move up/left/right/down)

#f-value function = infinity
#h-val + g-val

# tree pointer (x, y)
# point to previous node (coordinates)

#open list = start with start node
#search pq with a binary heap (heapq module)
#priority value is smallest f value


#closed list
#set of tuples (x, y)

#[Part 2]
#tiebreak function (favor larger g)
#tiebreak function (favor smaller g) RIGHT ANSWER

#Log which cells it explores

#Line 13

#State should be defined as (x, y)
#Find action spaces (up/left/right/down)
    #Check Bounds & check wall


""" IF YOU WANT TO TEST GET_NEIGHBORS
def test_get_neighbors():
    global grid
    grid = [['0' for _ in range(5)] for _ in range(5)]  # Create a 5x5 grid
    grid[0][1] = 'X'
    grid[1][0] = 'X'
    grid[2][0] = 'X'
    grid[2][1] = 'X'
    grid[2][2] = 'X'
    
    # Print the grid for reference
    for row in grid:
        print(' '.join(row))
    print()

    # Test get_neighbors on some cells
    test_cases = [(0, 0), (0, 2), (2, 2), (4, 4)]
    for row, col in test_cases:
        neighbors = get_neighbors(State(Cell(row, col, '0'), g=0, h=0))
        print(f"Neighbors of ({row}, {col}): {[(n.cell.x, n.cell.y) for n in neighbors]}")

test_get_neighbors()
"""
import numpy as np
import heapq
import random
from GridWorld import GridWorld


class Cell:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type

class State:
    def __init__(self, cell, g=np.inf, h=0):
        self.cell = cell
        self.g = g
        self.h = h
        self.f = self.g + self.h
        self.parent = None

    def __lt__(self, other):
        return self.f < other.f

def get_neighbors(state):
    row, col = state.cell.x, state.cell.y
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    neighbors = [(row + dr, col + dc) for dr, dc in directions]
    return [State(grid[r][c], g=np.inf, h=np.inf) for r, c in neighbors if is_valid((r, c))]

def is_valid(cell):
    row, col = cell
    return 0 <= row < 11 and 0 <= col < 11 and grid[row][col].type != 'X'

def heuristic(state, end_state):
    # Use Manhattan distance for heuristic
    return abs(state.cell.x - end_state.cell.x) + abs(state.cell.y - end_state.cell.y)

# def create_grid(rows, cols, obstacle_probability):
#     grid = []
#     for i in range(rows):
#         grid_row = []
#         for j in range(cols):
#             if np.random.random() < obstacle_probability:
#                 cell_type = 'X'
#             else:
#                 cell_type = '0'
#             grid_row.append(Cell(i, j, cell_type))
#         grid.append(grid_row)
#     return grid

def print_grid(grid):
    for row in grid:
        for cell in row:
            print(cell.type, end=" ")
        print()

def print_path(grid, path):
    path_cells = {cell for cell in path}
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            cell = grid[row][col]
            if cell in path_cells:
                print('P', end=' ')
            elif cell.type == 'X':
                print('X', end=' ')
            else:
                print(' ', end=' ')
        print()

def reconstruct_path(state):
    path = []
    while state is not None:
        path.append(state.cell)
        state = state.parent
    return path[::-1]

def backward_astar(grid, start_cell, end_cell, max_iterations=10000):
    # Initialize start and end States
    start_state = State(start_cell, g=0)
    end_state = State(end_cell, g=np.inf, h=0)  # h is 0 for the goal state

    start_state.h = heuristic(start_state, end_state)

    # Open and closed lists, stored as sets for efficient search
    open_list = {start_state}
    closed_list = set()

    iterations = 0

    while open_list and iterations < max_iterations:
        # Pop a state with the smallest f-value
        current_state = min(open_list, key=lambda state: state.f)
        open_list.remove(current_state)

        if current_state.cell == end_state.cell:
            print("Target Reached")
            return reconstruct_path(current_state)

        closed_list.add(current_state)

        for neighbor in get_neighbors(current_state):
            if neighbor in closed_list:
                continue
            tentative_g = current_state.g + 1  # assuming cost=1 for each step

            if neighbor not in open_list:
                open_list.add(neighbor)
            elif tentative_g >= neighbor.g:
                continue  # this is not a better path

            # This is the best path until now. Record it
            neighbor.parent = current_state
            neighbor.g = tentative_g
            neighbor.h = heuristic(neighbor, end_state)
            neighbor.f = neighbor.g + neighbor.h

        iterations += 1

    # No path found
    if iterations == max_iterations:
        print("Max Iterations Reached")
    else:
        print("No Path Found")
    return None

def test_backward_astar():
    global grid

    valid_gridworlds_arr = []
    while len(valid_gridworlds_arr) < 1:
        x = GridWorld(21, 21)
        x.make_grid()
        x.is_valid_grid_world()
        if(x.valid_grid_world):
            valid_gridworlds_arr.append(x)
    # for i in range(1):
    example_grid = valid_gridworlds_arr[0]
    start_cell = Cell(20, 20, " ")
    end_cell = Cell(20, 20, " ")
    example_grid.print_grid()

    grid = example_grid.grid

    path = backward_astar(example_grid.grid, start_cell, end_cell)

    if path is None:
        print("No Path Found")
        print_grid(example_grid.grid)
    else:
        print("Target Reached")
        print_path(example_grid.grid)

if __name__ == "__main__":
    test_backward_astar()
