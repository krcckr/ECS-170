######################################################################
## I was not able to complete the final function.
## But I have my fucntion framework all written.
## Just too hard for me implementing such a function as a beginner.
## I have tired my best. But only generate_new_states function works.
######################################################################



import copy


def rushhour(k, start_state):
    print("Total moves:", total_moves)
    print("Total states explored:", states_explored)
    return Asatrt_search(k, start_state)

def Astar_search(k,start_states):
    queue = [start_state]  # initialize the queue bfs search
    while queue:
        total_move+=1  
        if cur_state[2] == '----XX':  # check if the current state reaches the goal states
            return path
        else:
            k = heuristic(cur_state) # find the state with the lowest k but i dont know how to implement it so I just remain the rest of search function blank
            

## My heuristic function is counting the number of blocking plus the number of blocking of blocking           
def heuristic(cur_state):
    return (blocks(cur_state) + blocks_of_blocks(cur_state))

def blocks(cur_state):
    third_row = lsit(curr_sate[2])
    for i in range(0,4):
        if(third_row[i] == 'X'):  # locate 'X'
            X_end = i+1
    for j in range(X-end, 5):
        if(third_row[j].isalpha()):  # Count the number of vehicles blocking infront of the 'X'
            blocks_num+=1
    return blocks_num

def blocks_of_blocks(cur_state):
    third_row = lsit(curr_sate[2])
    for i in range(0,4):
        if(third_row[i] == 'X'):  
            X_end = i+1
    for j in range(X-end, 5):
        if(third_row[j].isalpha()):  # Find the number of column containing block
            block_letter = third_row[j]  # Store the letter that represent the block    
            for m in rang(0,5):
                if(cur_state[m][j].isalpha() and cur_state[m][j] != block_letter):  # Count the number of vehicles blocking the blocking vehicles
                    bob_num+=1
    return bob_num
    
    

## Generate all possible moves
def Trunk_right(cur_state):
    result = []
    for i in range(0,5):
        for j in range(0,2):  # set j 0 to 2 to avoid index out of range
            if(cur_state[i][j].isalpha()):  # Locate the head of a trunk
                List = list(cur_state[i])  # Change the string to list first bc strings are immutable in python
                letter = List[j]  # Store the letter that represent the trunk
                if(List[j+1] == List[j+2] == letter and List[j+3] == '-'):  # Determine if the trunk can move left
                    cur_statecp = copy.deepcopy(cur_state)
                    List[j] = '-'
                    List[j+3] = letter
                    cur_statecp[i] = "".join(List)  # Change the list back to string
                    result.append(cur_statecp)
    return(result)

###################################################
##All the following moves are implemented in
##the same way as the first so I won't repeat them
###################################################

def Trunk_left(cur_state):  
    result = []
    for i in range(0,5):
        for j in range(1,4):
            if(cur_state[i][j].isalpha()): 
                List = list(cur_state[i])  
                letter = List[j]  
                if(List[j+1] == List[j+2] == letter and List[j-1] == '-'): 
                    cur_statecp = copy.deepcopy(cur_state)
                    List[j-1] = letter
                    List[j+2] = '-'
                    cur_statecp[i] = "".join(List)  
                    result.append(cur_statecp)
    return(result)

def Trunk_down(cur_state):
    result = []
    for i in range(0,2):
        for j in range(0,5):
            if(cur_state[i][j].isalpha()): 
                letter = cur_state[i][j]
                if(cur_state[i+1][j] == cur_state[i+2][j] == letter and cur_state[i+3][j] == '-'):
                    cur_statecp = copy.deepcopy(cur_state)
                    upper = list(cur_state[i])
                    lower = list(cur_state[i+3])
                    upper[j] = '-'
                    lower[j] = letter
                    cur_statecp[i] = "".join(upper)
                    cur_statecp[i+3] = "".join(lower)
                    result.append(cur_statecp)
    return(result)

def Trunk_up(cur_state):
    result = []
    for i in range(1,3):
        for j in range(0,5):
            if(cur_state[i][j].isalpha()): 
                letter = cur_state[i][j]
                if(cur_state[i+1][j] == cur_state[i+2][j] == letter and cur_state[i-1][j] == '-'):
                    cur_statecp = copy.deepcopy(cur_state)
                    upper = list(cur_state[i-1])
                    lower = list(cur_state[i+2])
                    upper[j] = letter
                    lower[j] = '-'
                    cur_statecp[i-1] = "".join(upper)
                    cur_statecp[i+2] = "".join(lower)
                    result.append(cur_statecp)
    return(result)

def Car_right(cur_state):
    result = []
    for i in range(0,5):
        for j in range(0,3):
            if(cur_state[i][j].isalpha()):  
                List = list(cur_state[i])  
                letter = List[j] 
                if(List[j] == List[j+1] == letter and List[j+2] == '-'): 
                    cur_statecp = copy.deepcopy(cur_state)
                    List[j] = '-'
                    List[j+2] = letter
                    cur_statecp[i] = "".join(List)  
                    result.append(cur_statecp)
    return(result)

def Car_left(cur_state):
    result = []
    for i in range(0,5):
        for j in range(1,5):
            if(cur_state[i][j].isalpha()):  
                List = list(cur_state[i])  
                letter = List[j] 
                if(List[j] == List[j+1] == letter and List[j-1] == '-'): 
                    cur_statecp = copy.deepcopy(cur_state)
                    List[j-1] = letter
                    List[j+1] = '-'
                    cur_statecp[i] = "".join(List)  
                    result.append(cur_statecp)
    return(result)

def Car_down(cur_state):
    result = []
    for i in range(0,3):
        for j in range(0,5):
            if(cur_state[i][j].isalpha()): 
                letter = cur_state[i][j]
                if(cur_state[i][j] == cur_state[i+1][j] == letter and cur_state[i+2][j] == '-'):
                    cur_statecp = copy.deepcopy(cur_state)
                    upper = list(cur_state[i])
                    lower = list(cur_state[i+2])
                    upper[j] = '-'
                    lower[j] = letter
                    cur_statecp[i] = "".join(upper)
                    cur_statecp[i+2] = "".join(lower)
                    result.append(cur_statecp)
    return(result)

def Car_up(cur_state):
    result = []
    for i in range(1,4):
        for j in range(0,5):
            if(cur_state[i][j].isalpha()): 
                letter = cur_state[i][j]
                if(cur_state[i][j] == cur_state[i+1][j] == letter and cur_state[i-1][j] == '-'):
                    cur_statecp = copy.deepcopy(cur_state)
                    upper = list(cur_state[i-1])
                    lower = list(cur_state[i+1])
                    upper[j] = letter
                    lower[j] = '-'
                    cur_statecp[i-1] = "".join(upper)
                    cur_statecp[i+1] = "".join(lower)
                    result.append(cur_statecp)
    return(result)

    
def generate_new_states(cur_state):
    return(Trunk_right(cur_state)+Trunk_left(cur_state)+Trunk_up(cur_state)+Trunk_down(cur_state)+Car_right(cur_state)+Car_left(cur_state)+Car_down(cur_state)+Car_up(cur_state))
