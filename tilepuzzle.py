##-------------------------------------------------------------------------------------------------------
##--I implement generateNewStates function to generate all possible states.
##--But the program throws an error when statesearch function recursively calls my generateNewStates func.
##--I spent the whole 6 hours and couldn't find the problem.
##--I have a lot of other homework to do. It's a pity I didn't complete this program.
##--But the generateNewStates function works well. You can test it however you want.
##-------------------------------------------------------------------------------------------------------

def tilepuzzle(start,goal,k):
    return reverse(statesearch([start],goal,[],k))

def statesearch(unexplored,goal,path,k):
    ##--Add a for loop to limit the number of times the function is called
    for i in range (0,k):
        if unexplored == []:
            return []
        elif goal == head(unexplored):
            return cons(goal,path)
        else:       
            result = statesearch(generateNewStates(head(unexplored)),
                                 goal,
                                 cons(head(unexplored), path),k)
            if result != []:
                return result
            else:
                return statesearch(tail(unexplored),
                                   goal,
                                   path,k)

##-- Generate all possible displacements of 0

import copy

def generateZeroMoveUp(currState):
    result = []
    for i in range(1,3):
        for j in range(0,3):
            ##--Locate the position of "0"
            if currState[i][j] == 0:
                #Generate an list that is same as the original list
                currStatecopy = copy.deepcopy(currState)
                ##--Swap the position of "0" and the number above it
                currStatecopy[i-1][j], currStatecopy[i][j] = currStatecopy[i][j], currStatecopy[i-1][j]
                result.append(currStatecopy)
                break
    return(result)


def generateZeroMoveDown(currState):
    result = []
    for i in range(0,2):
        for j in range(0,3):
            if currState[i][j] == 0:
                currStatecopy = copy.deepcopy(currState)
                currStatecopy[i+1][j], currStatecopy[i][j] = currStatecopy[i][j], currStatecopy[i+1][j]
                result.append(currStatecopy)
                break
    return(result)


def generateZeroMoveRight(currState):
    result = []
    for i in range(0,3):
        for j in range(0,2):
            if currState[i][j] == 0:
                currStatecopy = copy.deepcopy(currState)
                currStatecopy[i][j+1], currStatecopy[i][j] = currStatecopy[i][j], currStatecopy[i][j+1]
                result.append(currStatecopy)
                break
    return(result)
 

def generateZeroMoveLeft(currState):
    result = []
    for i in range(0,3):
        for j in range(1,3):
            if currState[i][j] == 0:
                currStatecopy = copy.deepcopy(currState)
                currStatecopy[i][j], currStatecopy[i][j-1] =  currStatecopy[i][j-1], currStatecopy[i][j] 
                result.append(currStatecopy)
                break
    return(result)

##-- Here are some simple utility functions to give names to
##-- some of the list operations (borrowed from functional
##-- programming):

def reverse(st):
    return st[::-1]
    
def head(lst):
    return lst[0]

def tail(lst):
    return lst[1:]

def take(n,lst):
    return lst[0:n]

def drop(n,lst):
    return lst[n:]

def cons(item,lst):
    return [item] + lst

##--Finally put all of them together

def generateNewStates(currState):
    return(generateZeroMoveUp(currState)+generateZeroMoveRight(currState)+generateZeroMoveDown(currState)+generateZeroMoveLeft(currState))
    

