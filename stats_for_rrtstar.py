from MapEnvironment import MapEnvironment
from RRTStarPlanner import RRTStarPlanner
from matplotlib import pyplot as plt
import numpy as np

# def avg(x):
#     sum = 0
#     for number in x:
#         sum += number
#     return sum/len(x)

# def get_errors(x):
#     average = avg(x)
#     min = np.min(x)
#     max = np.max(x)
#     return (average-min, max-average)


# ext_mode = 'E2'
# planning_env = MapEnvironment("map2.json")

# stats_k2_cost = []
# stats_k2_time = []
# stats_k2_successes = 0

# stats_k3_cost = []
# stats_k3_time = []
# stats_k3_successes = 0

# stats_k5_cost = []
# stats_k5_time = []
# stats_k5_successes = 0

# stats_k10_cost = []
# stats_k10_time = []
# stats_k10_successes = 0

# stats_klog_cost = []
# stats_klog_time = []
# stats_klog_successes = 0


# for _ in range(10):
#     planner = RRTStarPlanner(planning_env, ext_mode, 0.05, k=2)

#     plan = planner.plan()
#     stats = planner.get_stats()

#     stats_k2_cost.append(stats['cost'])
#     stats_k2_time.append(stats['time'])

#     if stats['success']:
#         stats_k2_successes +=1

# print('k=2')
# print(f'cost = {stats_k2_cost}')
# print(f'time = {stats_k2_time}')
# print(f'total successes = {stats_k2_successes}')


# for _ in range(10):
#     planner = RRTStarPlanner(planning_env, ext_mode, 0.05, k=3)

#     plan = planner.plan()
#     stats = planner.get_stats()

#     stats_k3_cost.append(stats['cost'])
#     stats_k3_time.append(stats['time'])

#     if stats['success']:
#         stats_k3_successes +=1

# print('k=3')
# print(f'cost = {stats_k3_cost}')
# print(f'time = {stats_k3_time}')
# print(f'total successes = {stats_k3_successes}')

# for _ in range(10):
#     planner = RRTStarPlanner(planning_env, ext_mode, 0.05, k=5)

#     plan = planner.plan()
#     stats = planner.get_stats()

#     stats_k5_cost.append(stats['cost'])
#     stats_k5_time.append(stats['time'])

#     if stats['success']:
#         stats_k5_successes +=1

# print('k=5')
# print(f'cost = {stats_k5_cost}')
# print(f'time = {stats_k5_time}')
# print(f'total successes = {stats_k5_successes}')

# for _ in range(10):
#     planner = RRTStarPlanner(planning_env, ext_mode, 0.05, k=10)

#     plan = planner.plan()
#     stats = planner.get_stats()

#     stats_k10_cost.append(stats['cost'])
#     stats_k10_time.append(stats['time'])

#     if stats['success']:
#         stats_k10_successes +=1

# print('k=10')
# print(f'cost = {stats_k10_cost}')
# print(f'time = {stats_k10_time}')
# print(f'total successes = {stats_k10_successes}')

# for _ in range(10):
#     planner = RRTStarPlanner(planning_env, ext_mode, 0.05, k='Ologn')

#     plan = planner.plan()
#     stats = planner.get_stats()

#     stats_klog_cost.append(stats['cost'])
#     stats_klog_time.append(stats['time'])

#     if stats['success']:
#         stats_klog_successes +=1

# print('k=Ologn')
# print(f'cost = {stats_klog_cost}')
# print(f'time = {stats_klog_time}')
# print(f'total successes = {stats_klog_successes}')


# representative run of each k







ext_mode = 'E2'
planning_env = MapEnvironment("map2.json")
planner = RRTStarPlanner(planning_env, ext_mode, 0.05, k=2)

plan = planner.plan()
stats = planner.get_stats()

times_k2 = stats['time']
costs_k2 = stats['cost']

print('k2')
print(f'times_k2 = {times_k2}')
print(f'costs_k2 = {costs_k2}')

planner = RRTStarPlanner(planning_env, ext_mode, 0.05, k=3)

plan = planner.plan()
stats = planner.get_stats()

times_k3 = stats['time']
costs_k3 = stats['cost']

print('k3')
print(f'times_k3 = {times_k3}')
print(f'costs_k3 = {costs_k3}')

planner = RRTStarPlanner(planning_env, ext_mode, 0.05, k=5)

plan = planner.plan()
stats = planner.get_stats()

times_k5 = stats['time']
costs_k5 = stats['cost']

print('k5')
print(f'times_k5 = {times_k5}')
print(f'costs_k5 = {costs_k5}')

planner = RRTStarPlanner(planning_env, ext_mode, 0.05, k=10)

plan = planner.plan()
stats = planner.get_stats()

times_k10 = stats['time']
costs_k10 = stats['cost']

print('k10')
print(f'times_k10 = {times_k10}')
print(f'costs_k10 = {costs_k10}')



planner = RRTStarPlanner(planning_env, ext_mode, 0.05, k='Ologn')

plan = planner.plan()
stats = planner.get_stats()

times_klog = stats['time']
costs_klog = stats['cost']

print('klog')
print(f'times_klog = {times_klog}')
print(f'costs_klog = {costs_klog}')


plt.plot(times_k2, costs_k2)
plt.plot(times_k3, costs_k3)
plt.plot(times_k5, costs_k5)
plt.plot(times_k10, costs_k10)
plt.plot(times_klog, costs_klog)

plt.xlabel('time [s]')
plt.ylabel('cost of solution')
plt.legend(['k=2', 'k=3', 'k=5', 'k=10', 'k=O(log(n))'])

plt.show()

with open('RESULTS.txt', 'x') as f:
    f.write('k2\n')
    f.write(times_k2)
    f.write('\n')
    f.write(costs_k2)
    f.write('\n')

    f.write('k3\n')
    f.write(times_k3)
    f.write('\n')
    f.write(costs_k3)
    f.write('\n')

    f.write('k5\n')
    f.write(times_k5)
    f.write('\n')
    f.write(costs_k5)
    f.write('\n')

    f.write('k10\n')
    f.write(times_k10)
    f.write('\n')
    f.write(costs_k10)
    f.write('\n')

    f.write('klog\n')
    f.write(times_klog)
    f.write('\n')
    f.write(costs_klog)
    f.write('\n')
