import monkdata as m
import dtree as d
import copy

def printEntropy(dataset, nr):    
    # Print the entropy for the dataset
    print("Entropy(monk"+str(nr+1)+"): "+str(d.entropy(dataset)))

def getBestAttribute(dataset, attributes, available):
    # Returns the index of the best attribute to split on in attributes[]
    mostGain = -1;
    bestAttribute = None;
    for i in range(0, len(attributes)):
        if available[i] and d.averageGain(dataset, attributes[i]) > mostGain:
            mostGain = d.averageGain(dataset, attributes[i])
            bestAttribute = i
    return bestAttribute

def splitOnAttribute(dataset, attribute, doneSplits):
    sets = []
    for i in range(0, len(attribute.values)):
        sets.append(d.select(dataset, attribute, attribute.values[i]))
    return sets

def printEntropies(datasets):
    # Print the entropy for all datasets
    for i in range(0,len(datasets)):
        printEntropy(datasets[i], i)

def printGains(datasets, attributes):
    # Print GAIN for all datasets
    for i in range(0, len(datasets)):
        for j in range(0,len(attributes)):
            print("Gain monk"+str(i+1)+", a"+str(j+1)+": "+str(d.averageGain(datasets[i], attributes[j])))
        print("---------------")

def printGain(dataset, attributes):
    for j in range(0,len(attributes)):
            print("Gain a"+str(j+1)+": "+str(d.averageGain(dataset, attributes[j])))

def getNumTrue(dataset):
    # Return number of trues in the dataset
    numPos = 0
    for elem in dataset:
        if (elem.positive):
            numPos+=1
    return numPos

def getNumFalse(dataset):
    # Return number of false in dataset
    numNeg = 0
    for elem in dataset:
        if (not elem.positive):
            numNeg+=1
    return numNeg

def printNumTrueFalse(datasets):
    # For a list of datasets, print the number of true and false
    for i in range(0, len(datasets)):
        print("Monk"+str(i+1)+" "+
              "[#tot="+str(len(datasets[i]))+"] "+
              "[#true="+str(getNumTrue(datasets[i]))+"] "+
              "[#false="+str(getNumFalse(datasets[i]))+"]")
        
#Main
dataset = m.monk3
available = [True]*len(m.attributes)
firstSplit = getBestAttribute(dataset, m.attributes, available)
print("Firstsplit = "+str(firstSplit))
print("-----")
available[firstSplit] = False
sets = []
for i in range(0, len(m.attributes[firstSplit].values)):
    sets.append(d.select(dataset, m.attributes[firstSplit], m.attributes[firstSplit].values[i]))

for i in range(0, len(sets)):
    subSets = []
    splitOn = getBestAttribute(sets[i], m.attributes, available) 
    print("Second split = "+str(splitOn))
    for j in range(0, len(m.attributes[splitOn].values)):
        print(len(m.attributes[splitOn].values))
        #subSets.append(d.select(sets[i], m.attributes[i], m.attributes[i].values[j]))
    for s in subSets:
        print(d.mostCommon(s))

    print("----")

