import numpy as np
from RRTTree import RRTTree
import time
from MapEnvironment import MapEnvironment
from collections import deque
class RRTPlanner(object):

    def __init__(self, planning_env, ext_mode, goal_prob):

        # set environment and search tree
        self.planning_env = planning_env
        self.tree = RRTTree(self.planning_env)

        # set search params
        self.ext_mode = ext_mode
        self.goal_prob = goal_prob
        self.state_from_idx = {}
        self.stats = {}

    def plan(self):
        '''
        Compute and return the plan. The function should return a numpy array containing the states (positions) of the robot.
        '''

        start_time = time.time()

        # initialize an empty plan.
        plan = []

        # TODO: Task 4.4
        #update root(without check collusion):
        self.tree.add_vertex(self.planning_env.start)
        self.state_from_idx[0] = self.planning_env.start
        #update area limits
        x_range=self.planning_env.xlimit
        y_range = self.planning_env.ylimit
        #sample state:
        for i in range(4000): #number of iterations
            if (np.random.uniform(0, 1) < self.goal_prob): #bias goal
                #take target as sample
                a=self.planning_env.goal[0]
                b=self.planning_env.goal[1]
            else:
                a=np.random.uniform(x_range[0], x_range[1])
                b= np.random.uniform(y_range[0], y_range[1])
            new_state=np.array([a,b])
            x_near=self.tree.get_nearest_state(new_state)
            x_ext=self.extend(x_near[1],new_state).astype(int)
            if np.isnan(x_ext[0]): #same node
                continue
            ans2=MapEnvironment.edge_validity_checker(self.planning_env,x_near[1],x_ext)
            if ans2:
                x_new_idx=self.tree.add_vertex(x_ext)
                edge_cost=self.compute_cost([x_near[1],x_ext])
                self.tree.add_edge(x_near[0],x_new_idx,edge_cost)
                self.state_from_idx[x_new_idx] = x_ext

            if self.tree.is_goal_exists(self.planning_env.goal):
                break   

        plan = self.find_plan()
        self.stats['cost'] = self.compute_cost(plan)
        self.stats['time'] = time.time()-start_time
        
        # print total path cost and time
        print('Total cost of path: {:.2f}'.format(self.compute_cost(plan)))
        print('Total time: {:.2f}'.format(time.time()-start_time))

        # self.stats['cost'] = self.compute_cost(plan)
        # self.stats['time'] = time.time()-start_time

        return np.array(plan)

    def find_plan(self):
        if not self.tree.is_goal_exists(self.planning_env.goal):
            self.stats['success'] = False
            return []

        self.stats['success'] = True
        start_idx = self.tree.get_idx_for_state(self.planning_env.start)
        current_idx = self.tree.get_idx_for_state(self.planning_env.goal)
        
        print(f"length of dict = {len(self.state_from_idx)}")


        plan_indices = [current_idx]
        while current_idx != start_idx:
            current_idx = self.tree.edges[current_idx]
            plan_indices.append(current_idx)
        
        plan = []
        for idx in plan_indices:
            plan.append(self.state_from_idx[idx])

        print(f"plan = {plan}")
        return plan


    def compute_cost(self, plan):
        '''
        Compute and return the plan cost, which is the sum of the distances between steps.
        @param plan A given plan for the robot.
        '''
        total_cost=0
        # TODO: Task 4.4
        for i in range(len(plan)-1):
            total_cost+=MapEnvironment.compute_distance(self.planning_env,plan[i],plan[i+1])
        return total_cost

    def extend(self, near_state, rand_state):
        '''
        Compute and return a new position for the sampled one.
        @param near_state The nearest position to the sampled position.
        @param rand_state The sampled position.
        '''
        # TODO: Task 4.4
        step_size=10
        if self.ext_mode=='E1':
            return rand_state
        step_dir = np.array(rand_state) - np.array(near_state)
        length = np.linalg.norm(step_dir)
        #if new state enough close , leave it.
        step_dir = (step_dir / length) * min(step_size, length)  #check this is correct
        ext_state = np.asarray([int(near_state[0] + step_dir[0]), int(near_state[1] + step_dir[1])])
        return ext_state

    def get_stats(self):
        return self.stats



