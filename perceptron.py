import copy
## Generate a list. The element inside are the indices of '1' of the input array.
## Since 0 times any weights is 0, we dont need to consider the element of the input list with value 0        
def generateIndexList(list):        
    indexList = []
    for i in range(0,len(list)):
        if(list[i] == 1):
            indexList.append(i)
    return indexList

## Increase the weight of all specified indices by the amont of adjustment.
## The indexList is determined by generateIndexList() 
def increaseWeights(adjustment, weights, indexList): 
    for index in indexList:
        weights[index] += adjustment
    return weights

def decreaseWeights(adjustment, weights, indexList):
    for index in indexList:
        weights[index] -= adjustment
    return weights
    
    
## Generate one pass with and store the data in a list
def generatePass(threshold, adjustment, weights, examples):
    result = []
    for instance in examples:
        dict = {}
        answer = instance[0] ## The answer is always at the first position of a example list
        inputs = instance[1] ## The inputs is always at the second position of a example list
        indexList = generateIndexList(inputs)
        totalWeights = 0
        for index in indexList:
            totalWeights += weights[index]
        if(totalWeights <= threshold):
            prediction = False
        else:
            prediction = True
        if(prediction == False and answer == True): ## Whicih means the prediction is higher than expected. Thus decrease the weight
            weights = increaseWeights(adjustment, weights, indexList)
        elif(prediction == True and answer == False):
            weights = decreaseWeights(adjustment, weights, indexList)
        dict['inputs'] = inputs
        dict['prediction'] = prediction
        dict['answer'] = answer
        dict['adjusted_weights'] = weights
        dictCopy = copy.deepcopy(dict)
        result.append(dictCopy)
    return result
            
        
        
  
def perceptron(threshold, adjustment, weights, examples, passes):
    result = {}
    weight = copy.deepcopy(weights)
    thresholdCopy = copy.deepcopy(threshold)
    adjustmentCopy = copy.deepcopy(adjustment)
    result['init'] = {'weights': weight, 'threshold': thresholdCopy, 'adjustment': adjustmentCopy}
    for i in range(1,passes + 1):
        result[i] = generatePass(threshold, adjustment, weights, examples)
    return result
    
        








