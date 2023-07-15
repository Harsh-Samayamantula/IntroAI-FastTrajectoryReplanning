from GridWorld import GridWorld
import pickle
from a_star import forward_astar, backward_astar, test_backward_astar, test_forward_astar, set_tiebreak, adaptive_astar,test_adaptive_astar
import datetime
from statistics import mean

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
    


    # """ Repeated Forward A* being tested on the 50 pickled gridworlds """
    start_cell = (0, 0)
    end_cell = (100, 100)
    # count = 1
    # forward_astar_speed = []
    # for grid in retrieved_gridworlds_arr:
    #     start_time = datetime.datetime.now()
    #     forward_astar(grid.grid, grid.agent_grid, start_cell, end_cell)
    #     end_time = datetime.datetime.now()
    #     delta = (end_time - start_time).total_seconds()
    #     forward_astar_speed.append(delta)
    #     print(f"SCENARIO 1: Calculation to GRID #{count} is complete!")
    #     count+=1

    # with open('forward_a.pkl', 'wb') as f:
    #     pickle.dump(forward_astar_speed, f)

    """ Repeated Forward A* being tested with a favor smaller g heuristic on the 50 pickled gridworlds """
    # with open('gridworlds.pkl', 'rb') as f:
    #     retrieved_gridworlds_arr = pickle.load(f)
    # count = 1
    # forward_astar_smallg_speed = []
    # set_tiebreak(False)
    # for grid in retrieved_gridworlds_arr:
    #     start_time = datetime.datetime.now()
    #     forward_astar(grid.grid, grid.agent_grid, start_cell, end_cell)
    #     end_time = datetime.datetime.now()
    #     delta = (end_time - start_time).total_seconds()
    #     forward_astar_smallg_speed.append(delta)
    #     print(f"SCENARIO 2: Calculation to GRID #{count} is complete!")
    #     count+=1

    # with open('forward_a_small.pkl', 'wb') as f:
    #     pickle.dump(forward_astar_smallg_speed, f)

    """ Repeated Backward A* being tested on the 50 pickled gridworlds"""
    # start_cell = (0, 0)
    # end_cell = (100, 100)
    # set_tiebreak(True)
    # """ Starting with untraversed versions of gridworlds"""
    # count = 1
    # backward_astar_speed = []
    # with open('gridworlds.pkl', 'rb') as f:
    #     retrieved_gridworlds_arr = pickle.load(f)
    # for grid in retrieved_gridworlds_arr:
    #     start_time = datetime.datetime.now()
    #     backward_astar(grid.grid, grid.agent_grid, start_cell, end_cell)
    #     end_time = datetime.datetime.now()
    #     delta = (end_time - start_time).total_seconds()
    #     backward_astar_speed.append(delta)
    #     print(f"SCENARIO 3: Calculation to GRID #{count} is complete!")
    #     count+=1

    # with open('backward_a.pkl', 'wb') as f:
    #     pickle.dump(backward_astar_speed, f)

    """ Adaptive A* being tested on the 50 pickled gridworlds"""
    # count = 1
    # set_tiebreak(True)
    # adaptive_astar_speed = []
    # with open('gridworlds.pkl', 'rb') as f:
    #     retrieved_gridworlds_arr = pickle.load(f)
    # for grid in retrieved_gridworlds_arr:
    #     start_time = datetime.datetime.now()
    #     adaptive_astar(grid.grid, grid.agent_grid, start_cell, end_cell)
    #     end_time = datetime.datetime.now()
    #     delta = (end_time - start_time).total_seconds()
    #     adaptive_astar_speed.append(delta)
    #     print(f"SCENARIO 4: Calculation to GRID #{count} is complete!")
    #     count+=1
    
    # with open('adaptive_a.pkl', 'wb') as f:
    #     pickle.dump(adaptive_astar_speed, f)

    """ Repeated Backward A* being tested on the 50 pickled gridworlds"""
    # start_cell = (0, 0)
    # end_cell = (100, 100)
    # set_tiebreak(False)
    # """ Starting with untraversed versions of gridworlds"""
    # count = 1
    # backward_astar_smallg_speed = []
    # with open('gridworlds.pkl', 'rb') as f:
    #     retrieved_gridworlds_arr = pickle.load(f)
    # for grid in retrieved_gridworlds_arr:
    #     start_time = datetime.datetime.now()
    #     backward_astar(grid.grid, grid.agent_grid, start_cell, end_cell)
    #     end_time = datetime.datetime.now()
    #     delta = (end_time - start_time).total_seconds()
    #     backward_astar_smallg_speed.append(delta)
    #     print(f"SCENARIO 5: Calculation to GRID #{count} is complete!")
    #     count+=1

    # with open('backward_a_small.pkl', 'wb') as f:
    #     pickle.dump(backward_astar_smallg_speed, f)

    with open('backward_a.pkl', 'rb') as f:
        backward_astar_speed = pickle.load(f)
    with open('forward_a.pkl', 'rb') as f:
        forward_astar_speed = pickle.load(f)
    with open('forward_a_small.pkl', 'rb') as f:
        forward_astar_smallg_speed = pickle.load(f)
    with open('adaptive_a.pkl', 'rb') as f:
        adaptive_astar_speed = pickle.load(f)
    print(f'SUMMARY OF RESULTS \nForward A* (larger g tiebreak): {mean(forward_astar_speed)} \nForward A* (smaller g tiebreak): {mean(forward_astar_smallg_speed)} \nBackward A* (larger g tiebreak): {mean(backward_astar_speed)} \nAdaptive A*: {mean(adaptive_astar_speed)}')




if __name__ == "__main__":
    main()