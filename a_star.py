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
