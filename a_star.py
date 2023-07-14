
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
from prettytable import PrettyTable
import pickle

TIEBREAK_LARGER = True
class State:
    def __init__(self, x, y, g=np.inf, h=0):
        self.x = x
        self.y = y
        self.g = g
        self.h = h
        self.f = self.g + self.h
        self.parent = None

    def __eq__(self, other):
        if not isinstance(other, State):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __lt__(self, other):
        if self.f == other.f:
            if TIEBREAK_LARGER:
                return self.g > other.g #Tiebreak Favoring larger g
            else:
                return self.g < other.g
        return self.f < other.f

def get_neighbors(state, agent_grid):
    row, col = state.x, state.y
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    neighbors = [(row + dr, col + dc) for dr, dc in directions if is_valid((row + dr, col + dc), agent_grid)]
    # return [State(r, c, g=np.inf, h=np.inf) for r, c in neighbors]
    arr = [State(r, c, g=np.inf, h=np.inf) for r, c in neighbors]
    # for st in arr:
    #     print(st.x, st.y)
    return arr

def is_valid(cell, agent_grid):
    row, col = cell
    return 0 <= row < len(agent_grid) and 0 <= col < len(agent_grid[0]) and agent_grid[row][col] != 'X'


def in_bounds(x, y, grid):
    if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
        return True
    return False

def move_agent(current_state, path, grid, agent_grid):
    for move in path:
        update_visbility(current_state, grid, agent_grid)            
        if grid[move.x][move.y] == "X":
            #Print grid
            return current_state
        else:
            grid[current_state.x][current_state.y] = ' '
            grid[move.x][move.y] = 'A'
            current_state = move
    #Print Grid
    return current_state

def update_visbility(current_state, grid, agent_grid):
    x = current_state.x
    y = current_state.y
    if in_bounds(x, y+1,grid):
        if grid[x][y+1] == 'X' and agent_grid[x][y+1] == ' ':
            agent_grid[x][y+1] = 'X'
    if in_bounds(x, y-1,grid):
        if grid[x][y-1] == 'X' and agent_grid[x][y-1] == ' ':
            agent_grid[x][y-1] = 'X'
    if in_bounds(x+1, y,grid):
        if grid[x+1][y] == 'X' and agent_grid[x+1][y] == ' ':
            agent_grid[x+1][y] = 'X'
    if in_bounds(x-1, y,grid):
        if grid[x-1][y] == 'X' and agent_grid[x-1][y] == ' ':
            agent_grid[x-1][y] = 'X' 

def heuristic(state, end_state):
    # Use Manhattan distance for heuristic
    return abs(state.x - end_state.x) + abs(state.y - end_state.y)

def print_grid(grid):
    for row in grid:
        for cell in row:
            print(cell, end=" ")
        print()

def print_grid2(grid):
    x = PrettyTable()
    x.field_names = [f'{i}' for i in range(0, len(grid[0]))]
    x.add_rows(grid)
    print(x)

def print_path(grid, path):
    path_cells = {(state.x, state.y) for state in path}
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row, col) in path_cells:
                print('P', end=' ')
            elif grid[row][col] == 'X':
                print('X', end=' ')
            else:
                print(' ', end=' ')
        print()

def reconstruct_path(state):
    path = []
    while state is not None:
        path.append(state)
        state = state.parent
    return path[::-1]

def compute_path(agent_grid, c_state, end_state, open_list, closed_list, max_iterations):
    iterations = 0
    while open_list and iterations < max_iterations:
        # Pop a state with the smallest f-value
        c_state = min(open_list, key=lambda state: state.f)
        open_list.remove(c_state)

        if c_state.x == end_state.x and c_state.y == end_state.y:
            print('Path to target computed')
            return reconstruct_path(c_state)

        closed_list.add(c_state)
        
        for neighbor in get_neighbors(c_state, agent_grid):
            if neighbor in closed_list:
                continue
            tentative_g = c_state.g + 1  # assuming cost = 1 for each step

            if neighbor not in open_list:
                open_list.add(neighbor)
            elif tentative_g >= neighbor.g:
                continue

            # This is the best path until now. Record it
            neighbor.parent = c_state
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

def forward_astar(grid, agent_grid, start_cell, end_cell, max_iterations=10000):
      # Initialize the states without the heuristic
    start_state = State(start_cell[0], start_cell[1], g=0)
    end_state = State(end_cell[0], end_cell[1])

    # Now that both states exist, we can calculate and set the heuristic
    start_state.h = heuristic(start_state, end_state)
    end_state.h = heuristic(end_state, start_state)

    agent_state = start_state

    update_visbility(agent_state, grid, agent_grid)
    while agent_state.x != end_state.x or agent_state.y != end_state.y:
        open_list={agent_state}
        closed_list=set()
        path = compute_path(agent_grid, agent_state, end_state, open_list, closed_list, max_iterations)
        if not path:
            print("You've made a grave error. Max iterations reached")
            return False
        
        agent_state = move_agent(agent_state, path, grid, agent_grid)
    print_grid2(grid)
    print("Destination reached")
    return True
def backward_astar(grid, agent_grid, start_cell, end_cell, max_iterations=10000):
    start_state = State(start_cell[0], start_cell[1], g=0)
    end_state = State(end_cell[0], end_cell[1], g=np.inf)

    # agent_state = start_state
    agent_state = end_state
    end_state.h = heuristic(start_state, end_state) # Compute heuristic after end_state is assigned.

    update_visbility(agent_state, grid, agent_grid)
    while agent_state.x != end_state.x or agent_state.y != end_state.y:
        open_list={agent_state}
        # open_list = {end_state}
        closed_list=set()
        # path = compute_path(agent_grid, end_state, agent_state, open_list, closed_list, max_iterations)
        path = compute_path(agent_grid, agent_state, end_state, open_list, closed_list, max_iterations)
        print("OPEN")
        for s in open_list:
            print(s.x, s.y)
        print("CLOSED")
        for s in closed_list:
            print(s.x, s.y)  
        if not path:
            print("You've made a grave error. Max iterations reached")
            return False
        
        agent_state = move_agent(agent_state, path, grid, agent_grid)
        print_grid2(grid)
    print("Destination reached")
    return True

# def backward_astar(grid, start_cell, end_cell, max_iterations=10000):
#     # Initialize start and end States
#     start_state = State(start_cell[0], start_cell[1], g=0)
#     end_state = State(end_cell[0], end_cell[1], g=np.inf, h=0)  # h is 0 for the goal state

#     start_state.h = heuristic(start_state, end_state)

#     # Open and closed lists, stored as sets for efficient search
#     open_list = {start_state}
#     closed_list = set()

#     iterations = 0

#     while open_list and iterations < max_iterations:
#         # Pop a state with the smallest f-value
#         current_state = min(open_list, key=lambda state: state.f)
#         open_list.remove(current_state)

#         if current_state.x == end_state.x and current_state.y == end_state.y:
#             print("Target Reached")
#             return reconstruct_path(current_state)

#         closed_list.add(current_state)

#         for neighbor in get_neighbors(current_state):
#             if neighbor in closed_list:
#                 continue
#             tentative_g = current_state.g + 1  # assuming cost=1 for each step

#             if neighbor not in open_list:
#                 open_list.add(neighbor)
#             elif tentative_g >= neighbor.g:
#                 continue  # this is not a better path

#             # This is the best path until now. Record it
#             neighbor.parent = current_state
#             neighbor.g = tentative_g
#             neighbor.h = heuristic(neighbor, end_state)
#             neighbor.f = neighbor.g + neighbor.h

#         iterations += 1

#     # No path found
#     if iterations == max_iterations:
#         print("Max Iterations Reached")
#     else:
#         print("No Path Found")
#     return None

def test_forward_astar():
    valid_gridworlds_arr = []
    while len(valid_gridworlds_arr) < 1:
        x = GridWorld(101, 101)
        x.make_grid()
        x.is_valid_grid_world()
        if(x.valid_grid_world):
            valid_gridworlds_arr.append(x)

    example_grid = valid_gridworlds_arr[0]
    start_cell = (0, 0)
    end_cell = (100, 100)
    # example_grid.print_grid()

    # with open('gridworlds.pkl', 'rb') as f:
    #     retrieved_gridworlds_arr = pickle.load(f)
    
    # count = 0
    # for grid in retrieved_gridworlds_arr:
    #     forward_astar(grid.grid, grid.agent_grid, start_cell, end_cell)
    #     print(f"Calculation to GRID #{count} is complete!")
    #     count+=1
    # gridworld = retrieved_gridworlds_arr[40]
    
    forward_astar(example_grid.grid, example_grid.agent_grid, start_cell, end_cell)
    print_grid2(example_grid.grid)
    print('TEST COMPLETE')

def test_backward_astar():
    valid_gridworlds_arr = []
    while len(valid_gridworlds_arr) < 1:
        x = GridWorld(10, 10)
        x.make_grid()
        x.is_valid_grid_world()
        if(x.valid_grid_world):
            valid_gridworlds_arr.append(x)

    example_grid = valid_gridworlds_arr[0]
    start_cell = (9, 9)
    end_cell = (0, 0)
    backward_astar(example_grid.grid, example_grid.agent_grid, start_cell, end_cell)
    print_grid2(example_grid.grid)
    print('TEST COMPLETE')



def set_tiebreak(larger_g):
    global TIEBREAK_LARGER 
    TIEBREAK_LARGER = larger_g

if __name__ == "__main__":
    # test_backward_astar()
    test_forward_astar()