from MapEnvironment import MapEnvironment
from RRTPlanner import RRTPlanner
from matplotlib import pyplot as plt
import numpy as np

def avg(x):
    sum = 0
    for number in x:
        sum += number
    return sum/len(x)

def get_errors(x):
    average = avg(x)
    min = np.min(x)
    max = np.max(x)
    return (average-min, max-average)


ext_mode = 'E1'
planning_env = MapEnvironment("map2.json")

stats_E1_005_cost = []
stats_E1_005_time = []
stats_E1_005_successes = 0

stats_E2_005_cost = []
stats_E2_005_time = []
stats_E2_005_successes = 0

stats_E1_020_cost = []
stats_E1_020_time = []
stats_E1_020_successes = 0

stats_E2_020_cost = []
stats_E2_020_time = []
stats_E2_020_successes = 0

for _ in range(10):
    planner = RRTPlanner(planning_env, 'E1', 0.05)

    plan = planner.plan()
    stats = planner.get_stats()

    stats_E1_005_cost.append(stats['cost'])
    stats_E1_005_time.append(stats['time'])

    if stats['success']:
        stats_E1_005_successes +=1

print(f'total successes = {stats_E1_005_successes}')



for _ in range(10):
    planner = RRTPlanner(planning_env, 'E2', 0.05)

    plan = planner.plan()
    stats = planner.get_stats()

    stats_E2_005_cost.append(stats['cost'])
    stats_E2_005_time.append(stats['time'])

    if stats['success']:
        stats_E2_005_successes +=1

print(f'total successes = {stats_E2_005_successes}')

for _ in range(10):
    planner = RRTPlanner(planning_env, 'E1', 0.20)

    plan = planner.plan()
    stats = planner.get_stats()

    stats_E1_020_cost.append(stats['cost'])
    stats_E1_020_time.append(stats['time'])

    if stats['success']:
        stats_E1_020_successes +=1

print(f'total successes = {stats_E1_020_successes}')

for _ in range(10):
    planner = RRTPlanner(planning_env, 'E2', 0.20)

    plan = planner.plan()
    stats = planner.get_stats()

    stats_E2_020_cost.append(stats['cost'])
    stats_E2_020_time.append(stats['time'])

    if stats['success']:
        stats_E2_020_successes +=1

print(f'total successes = {stats_E2_020_successes}')

print(f'ahhh {stats_E1_005_cost}')

stats_E1_005_cost_avg = avg(stats_E1_005_cost)
stats_E1_005_time_avg = avg(stats_E1_005_time)
stats_E2_005_cost_avg = avg(stats_E2_005_cost)
stats_E2_005_time_avg = avg(stats_E2_005_time)
stats_E1_020_cost_avg = avg(stats_E1_020_cost)
stats_E1_020_time_avg = avg(stats_E1_020_time)
stats_E2_020_cost_avg = avg(stats_E2_020_cost)
stats_E2_020_time_avg = avg(stats_E2_020_time)

avgs = np.array([[stats_E1_005_cost_avg,
                stats_E1_005_time_avg],
                [stats_E2_005_cost_avg,
                stats_E2_005_time_avg],
                [stats_E1_020_cost_avg,
                stats_E1_020_time_avg],
                [stats_E2_020_cost_avg,
                stats_E2_020_time_avg]])



for item in avgs:
    plt.plot(item[0], item[1], 'o', linewidth=10)
legend=[]
strng = "E1, 5" + "%" + " bias"
legend.append(strng)
strng = "E2, 5" + "%" + " bias"
legend.append(strng)
strng = "E1, 20" + "%" + " bias"
legend.append(strng)
strng = "E2, 20" + "%" + " bias"
legend.append(strng)
plt.legend(legend)
plt.show()


print(f'averages = {avgs}')

print(stats_E1_005_cost)
print(stats_E1_005_time)
print(stats_E2_005_cost)
print(stats_E2_005_time)
print(stats_E1_020_cost)
print(stats_E1_020_time)
print(stats_E2_020_cost)
print(stats_E2_020_time)