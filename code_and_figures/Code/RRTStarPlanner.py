import numpy as np
from RRTTree import RRTTree
import time
from collections import deque
from MapEnvironment import MapEnvironment
import math
class RRTStarPlanner(object):

    def __init__(self, planning_env, ext_mode, goal_prob, k):

        # set environment and search tree
        self.planning_env = planning_env
        self.tree = RRTTree(self.planning_env)

        # set search params
        self.ext_mode = ext_mode
        self.goal_prob = goal_prob
        self.k = k

        self.stats = {}


    def plan(self):
        '''
        Compute and return the plan. The function should return a numpy array containing the states (positions) of the robot.
        '''
        start_time = time.time()

        # initialize an empty plan.
        plan = []

        # TODO: Task 4.4
        # update root(without check collusion):
        self.tree.add_vertex(self.planning_env.start)
        # update area limits
        x_range = self.planning_env.xlimit
        y_range = self.planning_env.ylimit
        costs = []
        times = []
        plan = []
        # sample state:
        for i in range(3000):  # number of iterations
            # print(f'iteration {i}')
            if (np.random.uniform(0, 1) < self.goal_prob):  # bias goal
                # take target as sample
                a = self.planning_env.goal[0]
                b = self.planning_env.goal[1]
            else:
                a = np.random.uniform(x_range[0], x_range[1])
                b = np.random.uniform(y_range[0], y_range[1])
            new_state = np.array([a, b])
            x_near = self.tree.get_nearest_state(new_state)
            x_ext = self.extend(x_near[1], new_state).astype(int)
            if np.isnan(x_ext[0]):  # same node
                continue
            ans2 = self.planning_env.edge_validity_checker(x_near[1], x_ext)
            if ans2:
                x_new_idx = self.tree.add_vertex(x_ext)
                edge_cost = self.planning_env.compute_distance(x_near[1], x_ext)
                self.tree.add_edge(x_near[0], x_new_idx, edge_cost)
                # k = math.ceil(np.log(len(self.tree.vertices.keys())))
                # k=min(5,len(self.tree.edges)) #constant

                if self.k == 'Ologn':
                    k = int(math.ceil(np.log(len(self.tree.vertices))))
                else:
                    k = int(self.k)
                
                k=min(k,len(self.tree.edges))
            

                if len(self.tree.edges)>1:
                    X_near = self.tree.get_k_nearest_neighbors(x_ext, k)
                    self.rewire_RRT_Star(X_near, x_ext)
                    X_near = self.tree.get_k_nearest_neighbors(x_ext, k)
                    self.second_rewire_RRT_Star(X_near, x_ext)
                    
            old_plan = plan

            # calculate plan
            plan = self.find_plan()

            costs.append(self.compute_cost(plan))
            times.append(time.time()-start_time)

            

        self.stats['cost'] = costs
        self.stats['time'] = times

        # print total path cost and time
        print('Total cost of path: {:.2f}'.format(self.compute_cost(plan)))
        print('Total time: {:.2f}'.format(time.time()-start_time))

        return np.array(plan)
        


    def rewire_RRT_Star(self, X_near, x_new):
        x_new_idx = self.tree.get_idx_for_state(x_new)
        best_neighbour_idx = None
        best_neighbour = None
        current_cost = self.tree.vertices[x_new_idx].cost

        for neighbour_idx, neighbour_state in zip(X_near[0], X_near[1]):
            if self.planning_env.edge_validity_checker(neighbour_state, x_new):
                potential_new_cost = self.tree.vertices[neighbour_idx].cost + self.planning_env.compute_distance(neighbour_state, x_new)
                if  potential_new_cost < current_cost:
                    current_cost = potential_new_cost
                    best_neighbour_idx = neighbour_idx
                    best_neighbour = neighbour_state

        if best_neighbour_idx is not None:
            self.tree.edges.pop(x_new_idx)
            edge_cost = self.planning_env.compute_distance(best_neighbour, x_new)
            self.tree.add_edge(best_neighbour_idx, x_new_idx, edge_cost)
    
    def second_rewire_RRT_Star(self, X_near, x_new):
        x_new_idx = self.tree.get_idx_for_state(x_new)

        for neighbour_idx, neighbour_state in zip(X_near[0], X_near[1]):
            current_cost = self.tree.vertices[neighbour_idx].cost
            if self.planning_env.edge_validity_checker(neighbour_state, x_new):
                potential_new_cost = self.tree.vertices[x_new_idx].cost + self.planning_env.compute_distance(neighbour_state, x_new)
                if  potential_new_cost < current_cost:
                    current_cost = potential_new_cost
                    self.tree.edges.pop(neighbour_idx)
                    edge_cost = self.planning_env.compute_distance(neighbour_state, x_new)
                    self.tree.add_edge(x_new_idx, neighbour_idx, edge_cost)

    def find_plan(self):
        if not self.tree.is_goal_exists(self.planning_env.goal):
            self.stats['success'] = False
            return []

        self.stats['success'] = True
        start_idx = self.tree.get_idx_for_state(self.planning_env.start)
        current_idx = self.tree.get_idx_for_state(self.planning_env.goal)

        plan = [self.tree.vertices[current_idx].state]
        while current_idx != start_idx:
            current_idx = self.tree.edges[current_idx]
            plan.append(self.tree.vertices[current_idx].state)

        # print(f"plan = {plan}")
        # print('found new plan')
        return plan


    def compute_cost(self, plan):
        '''
        Compute and return the plan cost, which is the sum of the distances between steps.
        @param plan A given plan for the robot.
        '''
        # TODO: Task 4.4
        total_cost=0
        for i in range(len(plan) - 1):
            total_cost += MapEnvironment.compute_distance(self.planning_env, plan[i], plan[i + 1])
        return total_cost

    def extend(self, near_state, rand_state):
        '''
        Compute and return a new position for the sampled one.
        @param near_state The nearest position to the sampled position.
        @param rand_state The sampled position.
        '''
        # TODO: Task 4.4
        step_size = 10
        if self.ext_mode == 'E1':
            return rand_state
        step_dir = np.array(rand_state) - np.array(near_state)
        length = np.linalg.norm(step_dir)
        # if new state enough close , leave it.
        step_dir = (step_dir / length) * min(step_size, length)
        ext_state = np.asarray([near_state[0] + step_dir[0], near_state[1] + step_dir[1]])
        return ext_state    

    def get_stats(self):
        return self.stats