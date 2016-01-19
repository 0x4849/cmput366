#-------------------------------
# Blackjack Lab - Programming Assignment 1
# Author: Brad Harrison
# Date: November 4th 2014
#-------------------------------

import blackjack
#from pylab import *
from numpy import *
import random

def gameStart():
  return blackjack.sample(0,1)

def giveSample(state):
  return blackjack.sample(state, giveAction())
  
def giveAction():
  return random.randint(0,1)

def anEpisode():
  reward, state = gameStart()
  
  if state == -1:
    return reward
  
  else:
    while state != -1:
      reward, state = giveSample(state)
      
    return reward

      
  
numEpisodes = 1000000

returnSum = 0.0
  

for episodeNum in range(numEpisodes):
    sampleReturn = anEpisode()
    
    
    #print "Episode: ", episodeNum, "Return: ", sampleReturn
    returnSum = returnSum + sampleReturn
print ("Average return: ", returnSum/numEpisodes)
