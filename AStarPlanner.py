import numpy as np
from heapdict import heapdict 

class AStarPlanner(object):    
    def __init__(self, planning_env):
        self.planning_env = planning_env

        # used for visualizing the expanded nodes
        # make sure that this structure will contain a list of positions (states, numpy arrays) without duplicates
        self.expanded_nodes = [] 
        self.open = {}
        self.close = {}
        # num_squares = (planning_env.xlimit[-1]+1)*(planning_env.ylimit[-1]+1)
        # self.parent = [None for _ in range(num_squares)]
        self.parent = {}
        self.epsilon = 20
        # self.g = [None for _ in range(num_squares)]
        # self.h = [None for _ in range(num_squares)]
        
    def plan(self):
        '''
        Compute and return the plan. The function should return a numpy array containing the states (positions) of the robot.
        '''

        #NOTE!!!! We Define our heapdicts in the following way:
        #open[state] = (state_vector, g, h)

        # initialize an empty plan.
        plan = []

        # TODO: Task 4.3
        start_state = self.planning_env.start
        self.open[tuple(start_state)] = (start_state, 0, self.get_h(start_state))

        while self.open:

            # test = self.open.popitem()
            # print(f"test = {test}")

            # _, (current_state, g, h) = self.open.popitem()
            (current_state, g, h) = self.pop_min(self.open)
            print(f"current state, g, h = {(current_state, g, h)}")


            #add current state to the list of expanded nodes for the visualization
            self.expanded_nodes.append(current_state)

            self.close[tuple(current_state)] = (current_state, g, h)

            if np.array_equal(current_state, self.planning_env.goal):
                print("reached here")
                # print(f"parents = {self.parent}")
                plan = self.get_plan()
                return np.array(plan)

            for neighbour_state in self.get_neighbours(current_state):
                print(f"neighbour state = {neighbour_state}")
                # self.parent[tuple(neighbour_state)] = current_state
                new_g = g + self.planning_env.compute_distance(current_state, neighbour_state)
                
                if (tuple(neighbour_state) not in self.open) and (tuple(neighbour_state) not in self.close):
                    self.parent[tuple(neighbour_state)] = current_state
                    self.open[tuple(neighbour_state)] = (neighbour_state, new_g, self.get_h(neighbour_state))

                elif (tuple(neighbour_state) in self.open):
                    g_neighbour = self.open[tuple(neighbour_state)][1]
                    h_neighbour = self.open[tuple(neighbour_state)][2]
                    if self.heuristic(new_g, h_neighbour) < self.heuristic(g_neighbour, h_neighbour):
                        # self.parent.pop(tuple(neighbour_state))
                        self.parent[tuple(neighbour_state)] = current_state
                        # self.open.pop(tuple(neighbour_state))
                        self.open[tuple(neighbour_state)] = (neighbour_state, new_g, h_neighbour)
                
                else: #neighbour in closed
                    g_neighbour = self.close[tuple(neighbour_state)][1]
                    h_neighbour = self.close[tuple(neighbour_state)][2]
                    if self.heuristic(new_g, h_neighbour) < self.heuristic(g_neighbour, h_neighbour):
                        self.parent[tuple(neighbour_state)] = current_state
                        self.close.pop(tuple(neighbour_state))
                        self.open[tuple(neighbour_state)] = (neighbour_state, new_g, h_neighbour)

        print("No solution found")
        return False

    def pop_min(self, state_dictionary):
        min_entry = None
        min_heuristic = np.inf

        for state_tuple in state_dictionary:
            g = state_dictionary[state_tuple][1]
            h = state_dictionary[state_tuple][2]
            heuristic = self.heuristic(g, h)
            if heuristic < min_heuristic:
                min_heuristic = heuristic
                min_entry = state_tuple

        return state_dictionary.pop(min_entry)

    def get_expanded_nodes(self):
        '''
        Return list of expanded nodes without duplicates.
        '''

        # used for visualizing the expanded nodes
        return self.expanded_nodes

    def get_plan(self):
        plan = []
        current_state = self.planning_env.goal

        while current_state is not self.planning_env.start:

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

