import numpy as np
from heapdict import heapdict 


class AStarPlanner(object):    
    def __init__(self, planning_env):
        self.planning_env = planning_env

        # used for visualizing the expanded nodes
        # make sure that this structure will contain a list of positions (states, numpy arrays) without duplicates
        self.expanded_nodes = [] 
        self.open = heapdict()
        self.close = heapdict()
        self.parent = {}
        self.g = {}
        self.epsilon = 20
        
    def plan(self):
        '''
        Compute and return the plan. The function should return a numpy array containing the states (positions) of the robot.
        '''
        # initialize an empty plan.
        plan = []

        # TODO: Task 4.3
        start_state = self.planning_env.start
        self.g[tuple(start_state)] = 0
        self.open[tuple(start_state)] = self.heuristic(0, self.get_h(start_state))

        while self.open:
            current_state, heuristic = self.open.popitem()
            current_state = np.array(current_state)

            #add current state to the list of expanded nodes for the visualization
            self.expanded_nodes.append(current_state)

            self.close[tuple(current_state)] = heuristic

            if np.array_equal(current_state, self.planning_env.goal):
                print("goal found")
                print(f"nodes expanded = {len(self.expanded_nodes)}")
                print(f"cost = {self.g[tuple(current_state)]}")
                plan = self.get_plan()
                return np.array(plan)

            for neighbour_state in self.get_neighbours(current_state):
                new_g = self.g[tuple(current_state)] + self.planning_env.compute_distance(current_state, neighbour_state)
                
                if (tuple(neighbour_state) not in self.open) and (tuple(neighbour_state) not in self.close):
                    self.parent[tuple(neighbour_state)] = current_state
                    self.g[tuple(neighbour_state)] = new_g
                    self.open[tuple(neighbour_state)] = self.heuristic(new_g, self.get_h(neighbour_state))

                elif (tuple(neighbour_state) in self.open):
                    current_heuristic = self.open[tuple(neighbour_state)]
                    if self.heuristic(new_g, self.get_h(neighbour_state)) < current_heuristic: #change this to just compare g's if still too slow
                        self.parent[tuple(neighbour_state)] = current_state
                        self.open.pop(tuple(neighbour_state))
                        self.g[tuple(neighbour_state)] = new_g
                        self.open[tuple(neighbour_state)] = self.heuristic(new_g, self.get_h(neighbour_state))
                
                else: #neighbour in closed
                    current_heuristic = self.close[tuple(neighbour_state)]
                    if self.heuristic(new_g, self.get_h(neighbour_state)) < current_heuristic: #change this to just compare g's if still too slow
                        self.parent[tuple(neighbour_state)] = current_state
                        self.close.pop(tuple(neighbour_state))
                        self.g[tuple(neighbour_state)] = new_g
                        self.close[tuple(neighbour_state)] = self.heuristic(new_g, self.get_h(neighbour_state))

        print("No solution found")
        return False

    def get_expanded_nodes(self):
        '''
        Return list of expanded nodes without duplicates.
        '''

        # used for visualizing the expanded nodes
        return self.expanded_nodes

    def get_plan(self):
        plan = []
        current_state = self.planning_env.goal

        while not np.array_equal(current_state, self.planning_env.start):

            plan.append(current_state)
            current_state = self.parent[tuple(current_state)]

        
        plan.append(current_state)


        plan.reverse()
        print(f"plan = {plan}")
        return plan


    def get_h(self, start_state):
        return self.planning_env.compute_distance(start_state, self.planning_env.goal)

    #IMPLEMENTED -- returns states in the 8 neighbouring squares. the states MUST be valid, otherwise are not returned
    def get_neighbours(self, state):
        neighbours = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    pass
                else:
                    step_vector = np.array([i, j])
                    new_state = state + step_vector
                    if self.planning_env.state_validity_checker(new_state):
                        neighbours.append(new_state)
        return neighbours

    def heuristic(self, g, h):
        return g + self.epsilon*h

