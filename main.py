from GridWorld import GridWorld
import pickle
from a_star import forward_astar, backward_astar, test_backward_astar, test_forward_astar, set_tiebreak


""" Used to generate 50 valid gridworlds --> stored in gridworlds.pkl """
def generate():
    valid_gridworlds_arr = []
    while len(valid_gridworlds_arr) < 50:
        x = GridWorld(101, 101)
        x.make_grid()
        # x.print_grid()
        x.is_valid_grid_world()
        if(x.valid_grid_world):
            valid_gridworlds_arr.append(x)
        print(f'SIZE OF VALID WORLDS: {len(valid_gridworlds_arr)}')


    with open('gridworlds.pkl', 'wb') as f:
        pickle.dump(valid_gridworlds_arr, f)

# Loading step
""" Retrieving the 50 generated valid gridworlds --> stored in gridworlds.pkl """
#with open('gridworlds.pkl', 'rb') as f:
#   retrieved_gridworlds_arr = pickle.load(f)
#print(len(retrieved_gridworlds_arr))
#Printing out a random one for sanity
#print(retrieved_gridworlds_arr[40].print_grid())


def main():
    # generate()
    with open('gridworlds.pkl', 'rb') as f:
        retrieved_gridworlds_arr = pickle.load(f)
    


    # """ Repeated Forward A* being tested on the 50 pickled gridworlds"""
    # start_cell = (0, 0)
    # end_cell = (100, 100)
    # count = 1
    # for grid in retrieved_gridworlds_arr:
    #     forward_astar(grid.grid, grid.agent_grid, start_cell, end_cell)
    #     print(f"Calculation to GRID #{count} is complete!")
    #     count+=1

    # """ Repeated Backward A* being tested on the 50 pickled gridworlds"""
    # start_cell = (100, 100)
    # end_cell = (0, 0)
    # """ Starting with untraversed versions of gridworlds"""
    # count = 1
    # with open('gridworlds.pkl', 'rb') as f:
    #     retrieved_gridworlds_arr = pickle.load(f)
    # for grid in retrieved_gridworlds_arr:
    #     backward_astar(grid.grid, grid.agent_grid, start_cell, end_cell)
    #     print(f"Calculation to GRID #{count} is complete!")
    #     count+=1

    # set_tiebreak(True)
    # test_forward_astar()
    # set_tiebreak(False)
    # test_forward_astar()
    set_tiebreak(True)
    test_backward_astar()
    set_tiebreak(False)
    test_backward_astar()
    



if __name__ == "__main__":
    main()