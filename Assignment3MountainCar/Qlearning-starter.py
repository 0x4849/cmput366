#-------------------------------
# MountainCar Lab - Programming Assignment 3
# Author: Brad Harrison
# Date: November 28th 2014
#-------------------------------

import mountaincar
from Tilecoder import numTilings, tilecode, numTiles
import Tilecoder
import numpy
import random
import pylab
#from pylab import *

def getQValues(weights):
    Q = numpy.zeros(3)
    Q[0] = dotProductReturn(weights,0)
    Q[1] = dotProductReturn(weights,1)
    Q[2] = dotProductReturn(weights,2)

    return Q

def getEGreedy():
    return random.uniform(0,1)
  
def eGreedy(array):
    eGreedyValue = getEGreedy()
    if eGreedyValue < EPSILON:
        return numpy.random.randint(0,3)
    else:
        return selectMaxAction(array)
     
def selectMaxAction(array):
    #print(array)
    return numpy.argmax(array)

def selectMaxActionValue(array):
    return array[numpy.argmax(array)]

def dotProductReturn(w, action):
    newArray = []
    x = numpy.zeros(n)
    if action == 0:
        newArray = listOfTiles[:]
            #listOfTiles = newArray
    elif action == 1:
        for index in listOfTiles:
            index = index + (4*9*9)
            newArray.append(index) 
                
    elif action == 2:
        for index in listOfTiles:
            index = index + (2*4*9*9)
                    #index = 2 * index
            newArray.append(index)
                
    x[newArray] = 1
    return numpy.dot(w,x)                

def writeF():
    fout = open('value', 'w')
    F = [0]*numTilings
    steps = 50
    for i in range(steps):
        for j in range(steps):
            tilecode(-1.2+i*1.7/steps, -0.07+j*0.14/steps, F)
            height = -max(Qs(F))
            fout.write(repr(height) + ' ')
        fout.write('\n')
    fout.close()

def savetxt(filename, theAverageReturnsArray):
    fout = open(filename, 'w')
    for index in theAverageReturnsArray:
        fout.write(repr(index) + ' ')
        fout.write('\n')        
    fout.close()

def writeAverages(filename,averages):
    savetxt(filename,averages)

def Qs(F):
    Q = [0,0,0]
    for action in range(3): 
        for index in F:
            Q[action] = Q[action] + w[index + (action*9*9*4)]
    return Q

#Best Settings found were alpha = 0.1 and lmbda = 0.95
numRuns = 50
numEpisodes = 200
alpha = 0.05/numTilings
GAMMA = 1
lmbda = 0.9
EPSILON = 0
n = numTiles * 3
zerovec = numpy.zeros(n)
listOfTiles = [-1]*numTilings

returnsArray = numpy.zeros((numRuns,numEpisodes))
runSum = 0.0
for run in range(numRuns):
    w = -0.01*pylab.rand(n)
    returnSum = 0.0
    for episodeNum in range(numEpisodes):
        G = 0
        state = mountaincar.init()
        e = numpy.zeros(n)
        steps = 0
        while state != None:
            Tilecoder.tilecode(state[0], state[1], listOfTiles)
            Q = getQValues(w)
            action = eGreedy(Q)
      
            reward, statePrime = mountaincar.sample(state, action)
            G = G + reward
            delta = reward - Q[action]
      
            for index in listOfTiles:
                e[(numTiles*action)+index] = 1   
    
            if statePrime == None:           
                for i in range(len(w)):
                    w[i] = w[i] + alpha * delta * e[i]
                    
                state = statePrime
                
            else:
                Tilecoder.tilecode(statePrime[0], statePrime[1], listOfTiles)
                Q = getQValues(w)              
                delta = delta + GAMMA * Q[numpy.argmax(Q)]
                
                for i in range(len(e)):
                    e[i] = e[i] * GAMMA * lmbda
                
                for i in range(len(w)):
                  w[i] = w[i] + alpha * delta * e[i]
                  
                state = statePrime
                steps = steps + 1
    
        returnsArray[run][episodeNum] = G     
        print("Episode: " +str(episodeNum)+ " Return: "+str(G)+" the steps was "+str(steps))
        returnSum = returnSum + G
    print("Average return:", returnSum/numEpisodes)
    runSum += returnSum
print("Overall average return:", runSum/numRuns/numEpisodes)


writeF()

standardDeviation = numpy.std(returnsArray)
standardError = standardDeviation / 7.0710678118654755 #For 50 runs. I actually have to manually input this value for sqrt(numRuns) because python seems to incorrectly divide if I don't.
averageReturns = numpy.mean(returnsArray)

print("The standard error was "+str(standardError))
print("The average return was "+str(averageReturns))
print("The alpha was "+str(alpha))
print("The lambda was "+str(lmbda))

averageReturnsArray = numpy.mean(returnsArray, axis = 0)
writeAverages('AverageReturns.txt', averageReturnsArray)


