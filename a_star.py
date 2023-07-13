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

class Cell:
    def __init__(self,x,y,type):
        self.x = x
        self.y = y
        self.type = type


class State:
    def __init__(self, cell, g=np.inf, h=0):
        self.cell = cell  # a Cell object that represents the current position
        self.g = g  # the cost to reach this state, set to infinity by default
        self.h = h  # heuristic value, set to 0 by default
        self.f = self.g + self.h  # total estimated cost of path through this state
        self.tree = None  # a pointer to the previous state (or None if this is the start state)
        self.search = 0  # a search-value, initialized as 0



def heuristic(state: State, end_state: State):
    # Use Manhattan distance for heuristic
    return abs(state.position[0] - end_state.position[0]) + abs(state.position[1] - end_state.position[1])


