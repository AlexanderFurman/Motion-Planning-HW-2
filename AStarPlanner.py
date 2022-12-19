import numpy as np
from heapdict import heapdict 

class AStarPlanner(object):    
    def __init__(self, planning_env):
        self.planning_env = planning_env

        # used for visualizing the expanded nodes
        # make sure that this structure will contain a list of positions (states, numpy arrays) without duplicates
        self.expanded_nodes = [] 
        self.open = heapdict.heapdict()
        self.close = heapdict.heapdict()

        num_squares = (planning_env.x_limit[-1]+1)*(planning_env.y_limit[-1]+1)
        self.parent = [None for _ in range(num_squares)]
        self.g = [None for _ in range(num_squares)]
        self.h = [None for _ in range(num_squares)]
        
    def plan(self):
        '''
        Compute and return the plan. The function should return a numpy array containing the states (positions) of the robot.
        '''

        # initialize an empty plan.
        plan = []

        # TODO: Task 4.3
        start_state = self.planning_env.start
        self.open[start_state] = self.planning_env.compute_heuristic(start_state)

        while self.open:
            (current_state, priority) = self.open.popitem()
            self.close[current_state] = priority
            for neighbour in self.get_neighbours(current_state):
                #YADA YADA FINISH THIS!
                pass

        return np.array(plan)

    def get_expanded_nodes(self):
        '''
        Return list of expanded nodes without duplicates.
        '''

        # used for visualizing the expanded nodes
        return self.expanded_nodes


    #IMPLEMENTED
    def get_neighbours(self, state):
        neighbours = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                step_vector = np.array(i, j)
                new_state = state + step_vector
                if self.planning_env.state_validity_checker(new_state):
                    neighbours.append(new_state)

