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
        self.parent = [None for _ in range(num_squares)]

        num_squares = (planning_env.x_limit[-1]+1)*(planning_env.y_limit[-1]+1)
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
        #open[state] = (state, g, h)
        self.open[start_state] = (start_state, 0, self.planning_env.compute_heursitic())

        while self.open:

            (current_state, g, h) = self.open.popitem()
            self.close[current_state] = (current_state, g, h)

            if current_state == self.planning_env.goal:
                plan = self.get_plan()
                return np.array(plan)

            for neighbour_state in self.get_neighbours(current_state):
                self.parent[neighbour_state] = current_state
                new_g = g + self.planning_env(current_state, neighbour_state)
                
                if (neighbour_state is not in self.open)

        return np.array(plan)

    def get_expanded_nodes(self):
        '''
        Return list of expanded nodes without duplicates.
        '''

        # used for visualizing the expanded nodes
        return self.expanded_nodes

    def get_plan(self):
        raise NotImplementedError()

    def cost_until_now(self, state):
        cost = 0
        while self.parent[state] is not None:




    #IMPLEMENTED
    def get_neighbours(self, state):
        neighbours = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                step_vector = np.array(i, j)
                new_state = state + step_vector
                if self.planning_env.state_validity_checker(new_state):
                    neighbours.append(new_state)

