# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from csv import reader

#################################------FROG------#####################################
class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        start = ['a', 'b', 'c', '_', 'x', 'y', 'z']
        
        return start
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        self.GS = ['x', 'y', 'z', '_', 'a', 'b', 'c']
        if (state == self.GS):
            return True
        else:
            return False
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        lst_successors = []
        index = state.index('_')
        
        if ((index-1 >= 0) and (state[index - 1] == 'a' or state[index - 1] == 'b' or state[index - 1] == 'c')):
            copy_state = state.copy()
            copy_state[index-1], copy_state[index] = copy_state[index], copy_state[index-1]
            tup = (copy_state, 'R', 1)
            lst_successors.append(tup)
        if ((index-2 >= 0) and (state[index - 2] == 'a' or state[index - 2] == 'b' or state[index - 2] == 'c')):
            copy_state = state.copy()
            copy_state[index-2], copy_state[index] = copy_state[index], copy_state[index-2]
            tup = (copy_state, '2R', 2)
            lst_successors.append(tup)
        if ((index+1 <= 6) and (state[index + 1] == 'x' or state[index + 1] == 'y' or state[index+1] == 'z')):
            copy_state = state.copy()
            copy_state[index+1], copy_state[index] = copy_state[index], copy_state[index+1]
            tup = (copy_state, 'L', 1)
            lst_successors.append(tup)
        if ((index+2 <= 6) and (state[index + 2] == 'x' or state[index + 2] == 'y' or state[index+2] == 'z')):
            copy_state = state.copy()
            copy_state[index+2], copy_state[index] = copy_state[index], copy_state[index+2]
            tup = (copy_state, '2L', 2)
            lst_successors.append(tup)

        return lst_successors
        util.raiseNotDefined()
        
    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        actionCost = 0
        if len(actions) == 0:
            return actionCost
        for i in actions:
            if (i == 'R' or i == 'L'):
                actionCost += 1
            else:
                actionCost += 2
        return actionCost
        util.raiseNotDefined()
        
    def getHeuristic(self,state):
        """
         state: the current state of agent

         THis function returns the heuristic of current state of the agent which will be the 
         estimated distance from goal.
        """
        heuristic = 0
        i = state.index('_')
        for i in range(3):
            if ((state[i] in 'xyz') != True) :
                heuristic+=1
            if ((state[i+4] in 'abc') != True):
                heuristic+=1
            if (state[3] != '_'):
                heuristic+=1
        return heuristic

##################################CITIES#########################################
class cities_problem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """
    def __init__(self):
        self.SS = input("Enter the starting city: ")
        self.GS = input("Enter the destination: ")
        self.connection_lst = []
        self.heuristics_lst = []
        with open('Connections.csv', 'r') as file:
            csv_reader = reader(file)
            for row in csv_reader:
                self.connection_lst.append(row)
        with open('heuristics.csv', 'r') as file2:
            csv_reader = reader(file2)
            for row in csv_reader:
                self.heuristics_lst.append(row)
        
    def getStartState(self):
        """
        Returns the start state for the search problem.
        """ 
        return self.SS
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        if (state == self.GS):
            return True
        else:
            return False
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        lst_successors = []
        for i in range(len(self.connection_lst)):
            if (self.connection_lst[i][0] == state):
                for j in range(1, len(self.connection_lst[i])):
                    if ((int(self.connection_lst[i][j]) == -1) or (int(self.connection_lst[i][j]) == 0)):
                        continue
                    else:
                        tup = (self.connection_lst[0][j], self.connection_lst[i][j], self.connection_lst[i][j])
                        lst_successors.append(tup)
                return lst_successors
        util.raiseNotDefined()
        
    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        actionCost = 0
        if len(actions) == 0:
            return actionCost
        for i in actions:
            actionCost += int(i)
        return actionCost
        util.raiseNotDefined()
        
    def getHeuristic(self,state):
        """
         state: the current state of agent

         THis function returns the heuristic of current state of the agent which will be the 
         estimated distance from goal.
        """
        SS_index = self.heuristics_lst[0].index(self.SS)
        CS_index = self.heuristics_lst[0].index(state)
        GS_index = self.heuristics_lst[0].index(self.GS)
        heuristic = int(self.heuristics_lst[SS_index][CS_index])
        return heuristic

#################################################################################

def aStarSearch(problem):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR A* CODE HERE ***"
    if problem == "frog":
        obj = SearchProblem()
    else:
        obj = cities_problem()
    open_lst = []
    CS = obj.getStartState()
    open_lst.append((0, CS))
    came_from = dict()
    cost_so_far = dict()
    CS2 = "".join(CS)
    came_from[CS2] = None
    cost_so_far[CS2] = 0
    final_states = []
    while (len(open_lst) > 0):
        open_lst.sort()
        (num, CS) = open_lst.pop(0)
        CS2 = "".join(CS)
        if (obj.isGoalState(CS) == True):
            break
        successor_lst = obj.getSuccessors(CS)
        for x,y,z in successor_lst:
            new_cost = cost_so_far[CS2] + int(z)
            x2 = "".join(x)
            if x2 not in cost_so_far or new_cost < cost_so_far[x2]:
                cost_so_far[x2] = new_cost
                priority = new_cost + obj.getHeuristic(x)
                open_lst.append((priority, x))
                came_from[x2] = CS2
    final_states.append("".join(CS))
    while (came_from[CS2] != None):
        final_states.append(came_from[CS2])
        CS2 = came_from[CS2]
    final_states = final_states[::-1]
    return final_states, cost_so_far["".join(obj.GS)]
    util.raiseNotDefined()

finalStates, cost = aStarSearch("cities")
print("Optimal path: ", finalStates)
print("Total Cost: ", cost)
