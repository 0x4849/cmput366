#-------------------------------
# Blackjack Lab - Programming Assignment 1
# Author: Brad Harrison
# Date: November 4th 2014
#-------------------------------

import blackjack
#from pylab import *
import numpy
import random
import sys
        
class QLearning:
        def __init__(self, epsilon, alpha, gamma, totalstates, totalactions, maxiterations, maxnumbersa, printEveryOneThousandEpisodes):
                self.EPSILON = epsilon
                self.ALPHA = alpha
                self.GAMMA = gamma
                self.TOTALSTATES = totalstates
                self.TOTALACTIONS = totalactions
                self.MAXITERATIONS = maxiterations
                self.MAXNUMBERSA = maxnumbersa
                self.printEveryOneThousandEpisodes = printEveryOneThousandEpisodes

                self.encountered =  numpy.ones(MAXNUMBERSA).reshape(TOTALSTATES,TOTALACTIONS)
                self.q = numpy.zeros(self.MAXNUMBERSA).reshape(self.TOTALSTATES,self.TOTALACTIONS)


        def gameStart(self):
          return blackjack.sample(0,1)

        def giveSample(self,state, action):
          return blackjack.sample(state, action)
          
        def giveAction(self):
          return random.randint(0,1)

        def getEGreedy(self):
          return random.random()
          
        def eGreedy(self,array,state):
          
          eGreedyValue = self.getEGreedy()

          if eGreedyValue < self.EPSILON:
            return numpy.random.randint(0,2)
          else:
            return self.maxAction(array,state)
             

        '''find max action in array q given state'''
        def maxAction(self,array,state):
          return numpy.argmax(array[state])

        def printPolicy2(self,s):
          theMaxAction = self.maxAction(self.q,s)
          return theMaxAction
          
        def onlyExploitQ(self):          
          iterations = 0
          returnSum = 0
          
          while iterations < self.MAXITERATIONS:
            s = blackjack.init()
            reward, state = blackjack.sample(s,1)
            if state == -1:
              returnSum = returnSum+reward
            while state != -1:
              A = self.maxAction(self.q, state)
              reward, statePrime = self.giveSample(state, A)
              returnSum = returnSum + reward

              state = statePrime
            iterations = iterations + 1
            if self.printEveryOneThousandEpisodes and iterations % 10000 == 0:
                print("Average Return During Exploitation Phase at "+str(iterations)+" is "+str(returnSum/iterations))
            
          return returnSum/self.MAXITERATIONS
          
        def getDynamicAlpha(self,state,action):
          newAlpha = 1/(self.encountered[state][action])
          self.encountered[state][action] = self.encountered[state][action] + 1
          return newAlpha

        def getAlpha(self):
                return self.ALPHA
          
        def aRandomState(self):
          return numpy.random.randint(1,181)
            
        def qLearning(self):
          for i in range(1,181):
            randomValue1 = random.random()
            randomValue2 = random.random()
            
            randomValue1 = randomValue1 * 0.00001
            randomValue2 = randomValue2 * 0.00001
            self.q[i][0] = randomValue1
            self.q[i][1] = randomValue2
          
          iterations = 0
          returnSum = 0
          while iterations < self.MAXITERATIONS:      
            s = blackjack.init()
            reward, state = blackjack.sample(s,1)
            if state == -1:
              returnSum = returnSum+reward
            while state != -1:
              A = self.eGreedy(self.q,state)
              reward, statePrime = self.giveSample(state, A)
              returnSum = returnSum + reward
              if reward == 0 and statePrime != -1:
                theMaxAction = self.maxAction(self.q, statePrime)
                newStateMaxQSA = self.q[statePrime][theMaxAction]
              else:
                newStateMaxQSA = 0
              
              if self.ALPHA == "Dynamic":
                      #print("YES")
                 ALPHA = self.getDynamicAlpha(state,A)
              else:
                 ALPHA = self.ALPHA

              bracketValue = reward+(self.GAMMA*newStateMaxQSA)-self.q[state][A]
              self.q[state][A] = self.q[state][A]+ALPHA*(bracketValue)  
              state = statePrime
            
            iterations = iterations + 1
            if self.printEveryOneThousandEpisodes and iterations % 10000 == 0:
                print("Average Return During Learning Phase at "+str(iterations)+" is "+str(returnSum/iterations))

          
          print("The Policy learned From the Exploration Phase is : ")
          blackjack.printPolicy(self.printPolicy2)
          return returnSum/self.MAXITERATIONS


GAMMA = 1.0
TOTALSTATES = 181 #0 to 180, there is no terminal state included.
TOTALACTIONS = 2
MAXITERATIONS = 1000000
MAXNUMBERSA = TOTALSTATES * TOTALACTIONS


#Beginning Part 2 of Assignment:
qLearnEquiProbable = QLearning(1.0, 0.001, GAMMA, TOTALSTATES, TOTALACTIONS, MAXITERATIONS, MAXNUMBERSA, False)
print("Doing the Beginning of Part 2 Assignment")
print("The equiprobable policy return for part 1 of assignment was : "+str(qLearnEquiProbable.qLearning()))
print("\n")

#Final Part 2 of Assignment
qLearnNext = QLearning(0.1, 0.001, GAMMA, TOTALSTATES, TOTALACTIONS, MAXITERATIONS, MAXNUMBERSA, True)
print("Doing Last stage of Part 2 of the Assignment -- Exploration Phase")
print("The average return in part 2 for learning phase alpha=0.001, gamma=0.1, episodes=1 million, is : "+str(qLearnNext.qLearning()))
print("\n")
print("Doing Part 2 of Assignment -- Exploitation Phase")
print("The average return in part 2 for exploitation phase alpha=0.001, gamma=0.1, episodes=1 million, is : "+str(qLearnNext.onlyExploitQ()))
print("\n")


#Part 3 of Assignment
qLearnFinal = QLearning(0.65, "Dynamic", GAMMA, TOTALSTATES, TOTALACTIONS, 10000000, MAXNUMBERSA, False)
print("Doing Part 3 of Assignment -- Exploration Phase")
print("The average return in part 3 for learning phase alpha=1/NumberTimesUpdated[State][Action] pair, epsilon=0.65, episodes=10 million, is : "+str(qLearnFinal.qLearning()))
print("\n")
print("Doing Part 3 of Assignment -- Exploitation Phase")
print("The average return in part 3 for exploitation phase alpha=1/NumberTimesUpdated[State][Action] pair, epsilon=0.65, episodes=10 million, is : "+str(qLearnFinal.onlyExploitQ()))




