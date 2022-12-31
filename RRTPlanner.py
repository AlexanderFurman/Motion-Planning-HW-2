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

    # def extend(self,x_new,eta=0.1):
    #     if self.ext_mode=="E1": #all the way connect
    #         return

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
        #update area limits
        x_range=self.planning_env.xlimit
        y_range = self.planning_env.ylimit
        #sample state:
        for i in range(300): #number of iterations
            if (np.random.uniform(0, 1) < self.goal_prob): #bias goal
                #take target as sample
                a=self.planning_env.goal[0]
                b=self.planning_env.goal[1]
            else:
                a=np.random.uniform(x_range[0], x_range[1])
                b= np.random.uniform(y_range[0], y_range[1])
            new_state=np.array([a,b])
            x_near=self.tree.get_nearest_state(new_state)
            x_ext=self.extend(x_near[1],new_state)
            if x_near[1][0] <0:
                a=88
            ans2=MapEnvironment.edge_validity_checker(self.planning_env,x_near[1],x_ext)
            if ans2:
                x_new_idx=self.tree.add_vertex(x_ext)
                edge_cost=self.compute_cost([x_near[1],x_ext])
                self.tree.add_edge(x_near[0],x_new_idx,edge_cost)

        #calculate plan
        if self.tree.is_goal_exists(self.planning_env.goal):
            print('goal exist')
            plan = self.dijkstra()

        # print total path cost and time
        print('Total cost of path: {:.2f}'.format(self.compute_cost(plan)))
        print('Total time: {:.2f}'.format(time.time()-start_time))

        return np.array(plan)

    def dijkstra(self):
        '''
        shortest path in the tree
        '''
        srcIdx = self.tree.get_root_id()
        dstIdx = self.tree.get_nearest_state(self.planning_env.goal)[0]

        # build dijkstra
        #edges = self.tree.get_edges_as_states()
        edges=self.tree.edges
        nodes = self.tree.vertices# list(G.neighbors.keys())
        nodes_list=list(nodes.keys())
        dist = {node: float('inf') for node in nodes_list}
        prev = {node: None for node in nodes_list}
        dist[srcIdx] = 0

        while nodes_list:
            curNode = min(nodes_list, key=lambda node: dist[node])
            nodes_list.remove(curNode)
            if dist[curNode] == float('inf'):
                break

            neighbors = [key for key, value in edges.items() if value == curNode ]
            for neighbor in neighbors:
                newCost = dist[curNode] + nodes[neighbor].cost
                if newCost < dist[neighbor]:
                    dist[neighbor] = newCost
                    prev[neighbor] = curNode

        #path
        path = deque()
        curNode = dstIdx
        while prev[curNode] is not None:
            path.appendleft(nodes[curNode].state)
            curNode = prev[curNode]
        path.appendleft(nodes[curNode].state)
        return list(path)

    def compute_cost(self, plan):
        '''
        Compute and return the plan cost, which is the sum of the distances between steps.
        @param plan A given plan for the robot.
        '''
        total_cost=0
        # TODO: Task 4.4
        for i in range(len(plan)-1):
            total_cost+=MapEnvironment.compute_distance(self.planning_env,plan[i],plan[i+1])
            #self.planning_env.co
        return total_cost

    def extend(self, near_state, rand_state):
        '''
        Compute and return a new position for the sampled one.
        @param near_state The nearest position to the sampled position.
        @param rand_state The sampled position.
        '''
        # TODO: Task 4.4
        step_size=1
        if self.ext_mode=='E1':
            return rand_state
        step_dir = np.array(rand_state) - np.array(near_state)
        length = np.linalg.norm(step_dir)
        #if new state enough close , leave it.
        step_dir = (step_dir / length) * min(step_size, length)
        ext_state=np.asarray([near_state[0] + step_dir[0], near_state[1] + step_dir[1]])
        return ext_state



