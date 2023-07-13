from GridWorld import GridWorld
import pickle


""" Used to generate 50 valid gridworlds --> stored in gridworlds.pkl """
# valid_gridworlds_arr = []
# while len(valid_gridworlds_arr) < 50:
#     x = GridWorld(101, 101)
#     x.make_grid()
#     x.print_grid()
#     x.is_valid_grid_world()
#     if(x.valid_grid_world):
#         valid_gridworlds_arr.append(x)


# with open('gridworlds.pkl', 'wb') as f:
#     pickle.dump(valid_gridworlds_arr, f)

# Loading step
""" Retrieving the 50 generated valid gridworlds --> stored in gridworlds.pkl """
#with open('gridworlds.pkl', 'rb') as f:
#   retrieved_gridworlds_arr = pickle.load(f)
#print(len(retrieved_gridworlds_arr))
#Printing out a random one for sanity
#print(retrieved_gridworlds_arr[40].print_grid())


def main():
    with open('gridworlds.pkl', 'rb') as f:
        retrieved_gridworlds_arr = pickle.load(f)
    

    gridworld = retrieved_gridworlds_arr[40]
    
    print(gridworld.print_grid())



if __name__ == "__main__":
    main()