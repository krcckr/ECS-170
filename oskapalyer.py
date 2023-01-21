import math
import copy

def whiteJump(state):
    result = []
    specialRow = int(len(state)/2) - 1 ## define a special row which seperate the game board in two parts
    for i in range(0,len(state)-2): ## -2 is to avoid index out of range
        for j in range(0,len(state[i])):
            if(state[i][j] == 'w'): ## Locate the position of white piece
                if(i < specialRow): ## For the pieces above the special row
                    if(j>=2 and state[i+1][j-1] == 'b' and state[i+2][j-2] == '-'): ## Check if the piece satisfies the condition to jump downward and left
                        stateCopy = copy.deepcopy(state)
                        list1 = list(state[i])     ## Change string to list sincce string is unchangable in python
                        list2 = list(state[i+1])
                        list3 = list(state[i+2])
                        list1[j] = '-'
                        list2[j-1] = '-'
                        list3[j-2] = 'w'
                        stateCopy[i] = "".join(list1)
                        stateCopy[i+1] = "".join(list2)
                        stateCopy[i+2] = "".join(list3)
                        result.append(stateCopy)
                    if(j < len(state[i+2]) and state[i+1][j] == 'b' and state[i+2][j] == '-'): ## Check if the piece satisfies the condition to jump downward and right
                        stateCopy = copy.deepcopy(state)
                        list1 = list(state[i])
                        list2 = list(state[i+1])
                        list3 = list(state[i+2])
                        list1[j] = '-'
                        list2[j] = '-'
                        list3[j] = 'w'
                        stateCopy[i] = "".join(list1)
                        stateCopy[i+1] = "".join(list2)
                        stateCopy[i+2] = "".join(list3)
                        result.append(stateCopy)
                elif(i > specialRow):  ## For the pieces under the special row
                    if(j + 2 < len(state[i+2]) and state[i+1][j+1] == 'b' and state[i+2][j+2] == '-'):## Check if the piece satisfies the condition to jump downward and right
                        stateCopy = copy.deepcopy(state)
                        list1 = list(state[i])
                        list2 = list(state[i+1])
                        list3 = list(state[i+2])
                        list1[j] = '-'
                        list2[j+1] = '-'
                        list3[j+2] = 'w'
                        stateCopy[i] = "".join(list1)
                        stateCopy[i+1] = "".join(list2)
                        stateCopy[i+2] = "".join(list3)
                        result.append(stateCopy)
                    if(j < len(state[i+2]) and state[i+1][j] == 'b' and state[i+2][j] == '-'):## Check if the piece satisfies the condition to jump downward and left
                        stateCopy = copy.deepcopy(state)
                        list1 = list(state[i])
                        list2 = list(state[i+1])
                        list3 = list(state[i+2])
                        list1[j] = '-'
                        list2[j] = '-'
                        list3[j] = 'w'
                        stateCopy[i] = "".join(list1)
                        stateCopy[i+1] = "".join(list2)
                        stateCopy[i+2] = "".join(list3)
                        result.append(stateCopy)
                else: ## Exhaustive list of all possible jumps at the special row
                    if(j == 0 and state[i+1][0] == 'b' and state[i+2][1] == '-'):
                        stateCopy = copy.deepcopy(state)
                        list1 = list(state[i])
                        list2 = list(state[i+1])
                        list3 = list(state[i+2])
                        list1[j] = '-'
                        list2[j] = '-'
                        list3[j+1] = 'w'
                        stateCopy[i] = "".join(list1)
                        stateCopy[i+1] = "".join(list2)
                        stateCopy[i+2] = "".join(list3)
                        result.append(stateCopy)
                    if(j == 1 and state[i+1][0] == 'b' and state[i+2][0] == '-'):
                        stateCopy = copy.deepcopy(state)
                        list1 = list(state[i])
                        list2 = list(state[i+1])
                        list3 = list(state[i+2])
                        list1[j] = '-'
                        list2[0] = '-'
                        list3[0] = 'w'
                        stateCopy[i] = "".join(list1)
                        stateCopy[i+1] = "".join(list2)
                        stateCopy[i+2] = "".join(list3)
                        result.append(stateCopy)
                    if(j == 1 and state[i+1][1] == 'b' and state[i+2][2] == '-'):
                        stateCopy = copy.deepcopy(state)
                        list1 = list(state[i])
                        list2 = list(state[i+1])
                        list3 = list(state[i+2])
                        list1[j] = '-'
                        list2[1] = '-'
                        list3[2] = 'w'
                        stateCopy[i] = "".join(list1)
                        stateCopy[i+1] = "".join(list2)
                        stateCopy[i+2] = "".join(list3)
                        result.append(stateCopy)
                    if(j == 2 and state[i+1][1] == 'b' and state[i+2][1] == '-'):
                        stateCopy = copy.deepcopy(state)
                        list1 = list(state[i])
                        list2 = list(state[i+1])
                        list3 = list(state[i+2])
                        list1[j] = '-'
                        list2[1] = '-'
                        list3[1] = 'w'
                        stateCopy[i] = "".join(list1)
                        stateCopy[i+1] = "".join(list2)
                        stateCopy[i+2] = "".join(list3)
                        result.append(stateCopy)
    return result

def whiteMove(state):
    result = []
    specialRow = int(len(state)/2)
    for i in range(0,len(state)-1): ## -1 to avoid index out of range
        for j in range(0,len(state[i])):
            if(state[i][j] == 'w'):
                if(i < specialRow):
                    if(j < len(state[i+1]) and state[i+1][j] == '-'): ## Check if there is empty space for the piece to move downward and right
                        stateCopy = copy.deepcopy(state)
                        list1 = list(state[i])
                        list2 = list(state[i+1])
                        list1[j] = '-'
                        list2[j] = 'w'
                        stateCopy[i] = "".join(list1)
                        stateCopy[i+1] = "".join(list2)
                        result.append(stateCopy)
                    if(j >= 1 and state[i+1][j-1] == '-'): ## Check if there is empty space for the piece to move downward and left
                        stateCopy = copy.deepcopy(state)
                        list1 = list(state[i])
                        list2 = list(state[i+1])
                        list1[j] = '-'
                        list2[j-1] = 'w'
                        stateCopy[i] = "".join(list1)
                        stateCopy[i+1] = "".join(list2)
                        result.append(stateCopy)
                else:
                    if(j < len(state[i+1]) and state[i+1][j] == '-'):## Check if there is empty space for the piece to move downward and left
                        stateCopy = copy.deepcopy(state)
                        list1 = list(state[i])
                        list2 = list(state[i+1])
                        list1[j] = '-'
                        list2[j] = 'w'
                        stateCopy[i] = "".join(list1)
                        stateCopy[i+1] = "".join(list2)
                        result.append(stateCopy)
                    if(j + 1 <= len(state[i+1]) and state[i+1][j+1] == '-'):## Check if there is empty space for the piece to move downward and right
                        stateCopy = copy.deepcopy(state)
                        list1 = list(state[i])
                        list2 = list(state[i+1])
                        list1[j] = '-'
                        list2[j+1] = 'w'
                        stateCopy[i] = "".join(list1)
                        stateCopy[i+1] = "".join(list2)
                        result.append(stateCopy)
                    
    return result


##The implementaion logic of black turn's move is same as white's.
##The only difference is the list indexing.
##And since black moves from bottom.
##So the if statements conditions are opposite form white's.
##So I just make no comment.

def blackJump(state):
    result = []
    specialRow = int(len(state)/2) + 1
    for i in range(2,len(state)):
        for j in range(0,len(state[i])):
            if(state[i][j] == 'b'):
                if(i < specialRow):
                    if(j + 2 < len(state[i-2]) and state[i-1][j+1] == 'w' and state[i-2][j+2] == '-'):
                        stateCopy = copy.deepcopy(state)
                        list1 = list(state[i])
                        list2 = list(state[i-1])
                        list3 = list(state[i-2])
                        list1[j] = '-'
                        list2[j+1] = '-'
                        list3[j+2] = 'b'
                        stateCopy[i] = "".join(list1)
                        stateCopy[i-1] = "".join(list2)
                        stateCopy[i-2] = "".join(list3)
                        result.append(stateCopy)
                    if(state[i-1][j] == 'w' and state[i-2][j] == '-'):
                        stateCopy = copy.deepcopy(state)
                        list1 = list(state[i])
                        list2 = list(state[i-1])
                        list3 = list(state[i-2])
                        list1[j] = '-'
                        list2[j] = '-'
                        list3[j] = 'b'
                        stateCopy[i] = "".join(list1)
                        stateCopy[i-1] = "".join(list2)
                        stateCopy[i-2] = "".join(list3)
                        result.append(stateCopy)
                elif(i > specialRow):
                    if(j >= 2 and state[i-1][j-1] == 'w' and state[i-2][j-2] == '-'):
                        stateCopy = copy.deepcopy(state)
                        list1 = list(state[i])
                        list2 = list(state[i-1])
                        list3 = list(state[i-2])
                        list1[j] = '-'
                        list2[j-1] = '-'
                        list3[j-2] = 'b'
                        stateCopy[i] = "".join(list1)
                        stateCopy[i-1] = "".join(list2)
                        stateCopy[i-2] = "".join(list3)
                        result.append(stateCopy)
                    if(j < len(state[i-2]) and state[i-1][j] == 'w' and state[i-2][j] == '-'):
                        stateCopy = copy.deepcopy(state)
                        list1 = list(state[i])
                        list2 = list(state[i-1])
                        list3 = list(state[i-2])
                        list1[j] = '-'
                        list2[j] = '-'
                        list3[j] = 'b'
                        stateCopy[i] = "".join(list1)
                        stateCopy[i-1] = "".join(list2)
                        stateCopy[i-2] = "".join(list3)
                        result.append(stateCopy)
                else:
                    if(j == 0 and state[i-1][0] == 'w' and state[i-2][1] == '-'):
                        stateCopy = copy.deepcopy(state)
                        list1 = list(state[i])
                        list2 = list(state[i-1])
                        list3 = list(state[i-2])
                        list1[j] = '-'
                        list2[0] = '-'
                        list3[1] = 'b'
                        stateCopy[i] = "".join(list1)
                        stateCopy[i-1] = "".join(list2)
                        stateCopy[i-2] = "".join(list3)
                        result.append(stateCopy)
                    if(j == 1 and state[i-1][0] == 'w' and state[i-2][0] == '-'):
                        stateCopy = copy.deepcopy(state)
                        list1 = list(state[i])
                        list2 = list(state[i-1])
                        list3 = list(state[i-2])
                        list1[j] = '-'
                        list2[0] = '-'
                        list3[0] = 'b'
                        stateCopy[i] = "".join(list1)
                        stateCopy[i-1] = "".join(list2)
                        stateCopy[i-2] = "".join(list3)
                        result.append(stateCopy)
                    if(j == 1 and state[i-1][1] == 'w' and state[i-2][2] == '-'):
                        stateCopy = copy.deepcopy(state)
                        list1 = list(state[i])
                        list2 = list(state[i-1])
                        list3 = list(state[i-2])
                        list1[j] = '-'
                        list2[1] = '-'
                        list3[2] = 'b'
                        stateCopy[i] = "".join(list1)
                        stateCopy[i-1] = "".join(list2)
                        stateCopy[i-2] = "".join(list3)
                        result.append(stateCopy)
                    if(j == 2 and state[i-1][1] == 'w' and state[i-2][1] == '-'):
                        stateCopy = copy.deepcopy(state)
                        list1 = list(state[i])
                        list2 = list(state[i-1])
                        list3 = list(state[i-2])
                        list1[j] = '-'
                        list2[1] = '-'
                        list3[1] = 'b'
                        stateCopy[i] = "".join(list1)
                        stateCopy[i-1] = "".join(list2)
                        stateCopy[i-2] = "".join(list3)
                        result.append(stateCopy)
    return result
                        
def blackMove(state):
    result = []
    specialRow = int(len(state)/2)
    for i in range(1,len(state)):
        for j in range(0,len(state[i])):
            if(state[i][j] == 'b'):
                if(i > specialRow):
                    if(j < len(state[i-1]) and state[i-1][j] == '-'):
                        stateCopy = copy.deepcopy(state)
                        list1 = list(state[i])
                        list2 = list(state[i-1])
                        list1[j] = '-'
                        list2[j] = 'b'
                        stateCopy[i] = "".join(list1)
                        stateCopy[i-1] = "".join(list2)
                        result.append(stateCopy)
                    if(j >= 1 and state[i-1][j-1] == '-'):
                        stateCopy = copy.deepcopy(state)
                        list1 = list(state[i])
                        list2 = list(state[i-1])
                        list1[j] = '-'
                        list2[j-1] = 'b'
                        stateCopy[i] = "".join(list1)
                        stateCopy[i-1] = "".join(list2)
                        result.append(stateCopy)
                else:
                    if(state[i-1][j] == '-'):
                        stateCopy = copy.deepcopy(state)
                        list1 = list(state[i])
                        list2 = list(state[i-1])
                        list1[j] = '-'
                        list2[j] = 'b'
                        stateCopy[i] = "".join(list1)
                        stateCopy[i-1] = "".join(list2)
                        result.append(stateCopy)
                    if(j + 1 <= len(state[i-1]) and state[i-1][j+1] == '-'):
                        stateCopy = copy.deepcopy(state)
                        list1 = list(state[i])
                        list2 = list(state[i-1])
                        list1[j] = '-'
                        list2[j+1] = 'b'
                        stateCopy[i] = "".join(list1)
                        stateCopy[i-1] = "".join(list2)
                        result.append(stateCopy)
                    
    return result


def movegen(state, turn):
    if(turn == 'w'): ## If it is white turn then call functions of white
        return(whiteJump(state)+whiteMove(state))
    elif(turn == 'b'):
        return(blackJump(state)+blackMove(state))
    else:
        return 0 ## Avoid crash if there is an invalid input

state = ['www-', '--w', '--', '---', 'bbb-']


###############################################
##Below is the code for my hw4. I applied minimax algorithm.
##But I don't know how to trace back to the original index of that optimal value.
##So my getindex function is blank
##############################################
def eval(state, maxPlayer):
    """
    the evaluation function  of a state
    """
    pieces = 0
    totalDistance = 0
    if(maxPlayer == 'w'):
        for i in range(0, len(state)):
            for j in range(0,len(state[i])):
                if(state[i][j] == 'w'):
                    distance = len(state) - i - 1 ## the distance is represented by the number of rows from the opposite side
                    pieces += 1 ## determine number of pieces remaining.
                    totalDistance += distance
    if(maxPlayer == 'b'):
        for i in range(0, len(state)):
            for j in range(0,len(state[i])):
                if(state[i][j] == 'b'):
                    distance = i
                    pieces += 1 
                    totalDistance += distance
    if(pieces == 0):
        return -math.inf ## prevent division by 0
    else:
        return (-totalDistance/pieces) ## Use the average distance as an evaluation. The smaller the average distance, the greater winning chance, Thus make it negtive.

def minimax(node, depth, ismaxTurn, maxPlayer):
    if(maxPlayer == 'b'): ## define who is max and min
        minPlayer = 'w'
    else:
        minPlayer = 'b'
        
    if(depth == 0 or movegen(node, maxPlayer) == []): ## if reaches the depth or node is a terminal node
        return eval(node, maxPlayer)
    elif(ismaxTurn):
        maxVal = -math.inf ## Set the initial value of max turn's node to -inf
        for child in movegen(node, maxPlayer): ## recursively call minimax on each child under each node 
            maxVal = max(maxVal,minimax(child, depth -1, False, maxPlayer)) ## Take the maximum value in the turn of max
            return maxVal
    else:
        minVal = math.inf
        for child in movegen(node, minPlayer): 
            minVal = min(minVal, minimax(child, depth -1, True, maxPlayer))
            return minVal

def getindex(state,depth, maxPlayer, optimalVal):
    """
    get the index of the optimal value generated by minimax search and trace back the index of the next move
    """
    return index
        
    
                
            
        
def oskaplayer(state, maxPlayer, depth):
    nextStates = movegen(state, maxPlayer)
    optimalVal = minimax(state, depth, True, maxPlayer)
    index = getindex(state, depth, maxPlayer, optimalVal)
    return nextStates[index]
    
     
     
     
    
    
        
        
        

        
        
    
    
                    
                    
                    
    



