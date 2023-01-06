from matplotlib import pyplot as plt
import numpy as np

#rrt info
# vec = np.array([[586.80601143,   1.68837094],
#                 [492.69475662,  10.00514636],
#                 [606.1041878,    2.24291778],
#                 [523.51949185,   6.9056639 ]])

# for item in vec:
#     plt.plot(item[0], item[1], 'o', linewidth=10)

# legend=[]
# strng = "E1, 5" + "%" + " bias"
# legend.append(strng)
# strng = "E2, 5" + "%" + " bias"
# legend.append(strng)
# strng = "E1, 20" + "%" + " bias"
# legend.append(strng)
# strng = "E2, 20" + "%" + " bias"
# legend.append(strng)
# plt.legend(legend)
# plt.show()



# stats_E1_005_cost=np.array([490.6631080069359, 542.7159816755428, 524.7420520526413, 599.9466990810233, 522.7201232379499, 670.3765118388588, 473.5398614486755, 849.1287305830846, 525.9226008503103, 597.4800689960775])
# stats_E1_005_time=np.array([0.41159653663635254, 1.960068941116333, 1.553246259689331, 0.8190932273864746, 0.3905465602874756, 0.3442237377166748, 0.4023430347442627, 6.721515655517578, 0.37128472328186035, 6.210450649261475])
# stats_E2_005_cost=np.array([490.36727211320056, 500.3257366078197, 554.0632088881998, 563.4150032841646, 650.8987242460645, 494.7266269867214, 438.51197107874526, 582.8837768340326, 521.1951947366357, 418.172605113528])
# stats_E2_005_time=np.array([10.95772647857666, 7.822743654251099, 7.103400707244873, 18.37932062149048, 9.353517293930054, 10.061092615127563, 6.622633218765259, 16.313377141952515, 11.128445148468018, 5.867043495178223])
# stats_E1_020_cost=np.array([456.9381337584669, 564.6691538170834, 535.89070798519, 533.4370085406897, 715.8648606531366, 635.6998419532914, 713.4668295343628, 576.7793072577815, 696.8505560616312, 550.6997858635889])
# stats_E1_020_time=np.array([1.2981352806091309, 0.3758566379547119, 1.2010877132415771, 0.9444756507873535, 0.15666985511779785, 0.8376049995422363, 5.547071218490601, 0.41207385063171387, 1.3760430812835693, 1.3285751342773438])
# stats_E2_020_cost=np.array([541.5781025871726, 481.9044288276331, 488.2834114084097, 510.2995729278886, 535.8897633949566, 637.2170126795146, 436.90104594402584, 532.4745216172801, 568.5285502780107, 502.11850879972866])
# stats_E2_020_time=np.array([8.788484334945679, 6.90174674987793, 4.132257461547852, 7.819355487823486, 6.752951145172119, 5.44377326965332, 6.230486631393433, 14.400963544845581, 3.1413767337799072, 5.44524359703064])


# costs = np.array([stats_E1_005_cost,
#                 stats_E2_005_cost,
#                 stats_E1_020_cost,
#                 stats_E2_020_cost])

# times = np.array([stats_E1_005_time,
#                 stats_E2_005_time,
#                 stats_E1_020_time,
#                 stats_E2_020_time])

# avg_costs = np.array([586.80601143,
#                         492.69475662,
#                         606.1041878, 
#                         523.51949185,])

# avg_times = np.array([1.68837094,
#                         10.00514636,
#                         2.24291778,
#                         6.9056639 ])



# #create cumulative distribution function

# time_steps = np.linspace(0,20,50)

# stats_time_number_successes = []

# for item in times:
#     count = 0
#     sub_array = []
#     for i in range(50):
#         for time_to_success in item:
#             if time_to_success <= time_steps[i]:
#                 count += 1
#         sub_array.append(count/10)
#         count = 0
#     stats_time_number_successes.append(sub_array)


# plt.plot(time_steps, stats_time_number_successes[0])
# plt.plot(time_steps, stats_time_number_successes[1])
# plt.plot(time_steps, stats_time_number_successes[2])
# plt.plot(time_steps, stats_time_number_successes[3])

# legend=[]
# strng = "E1, 5" + "%" + " bias"
# legend.append(strng)
# strng = "E2, 5" + "%" + " bias"
# legend.append(strng)
# strng = "E1, 20" + "%" + " bias"
# legend.append(strng)
# strng = "E2, 20" + "%" + " bias"
# legend.append(strng)
# plt.legend(legend)
# plt.xlabel('time [s]')
# plt.ylabel('success fraction')
# plt.show()



def avg(x):
    sum = 0
    for number in x:
        sum += number
    return sum/len(x)

# rrtstar info


k2_cost = [445.00383609796, 461.5657662257138, 539.7699862221373, 561.9017513065437, 485.3550601457664, 541.0186137455722, 592.4788374980702, 540.080051518701, 522.9211739286394, 544.8249051352616]
k2_time = [65.79745626449585, 77.00973439216614, 67.32489848136902, 58.543883085250854, 66.97078919410706, 58.96045207977295, 73.15810441970825, 70.06125020980835, 69.65052914619446, 68.60416340827942]

k3_cost = [429.53236569908836, 464.5674423583706, 513.15556294098, 457.77739807880266, 453.3014460204269, 544.917137759433, 456.73928585695165, 410.4684267040191, 437.2310945427633, 477.6348707908924]
k3_time = [67.68715167045593, 61.29961824417114, 67.49003529548645, 57.244933128356934, 64.76686215400696, 63.11515927314758, 75.03630590438843, 67.36006712913513, 71.04840207099915, 67.50588750839233]


k5_cost = [387.76547228020354, 360.48229799456095, 368.63935682603153, 379.3361672032092, 404.6037724896985, 426.5074497829484, 377.6411520163141, 376.96764109348163, 389.13059090617065, 397.1170022980689]
k5_time = [68.16901469230652, 65.37652230262756, 63.76695537567139, 67.10155701637268, 69.66996312141418, 66.09782338142395, 70.20557975769043, 69.80450701713562, 69.29857325553894, 68.29954886436462]

k10_cost = [369.23099479481556, 349.87729936532236, 355.5360803575822, 363.03714147645877, 364.1616877286314, 357.87310596470377, 354.35354757933834, 371.398323711439, 360.23913492473946, 361.14000712245837]
k10_time = [75.74520611763, 67.63172340393066, 64.52974891662598, 69.50216507911682, 72.01730251312256, 69.68714332580566, 57.81818985939026, 65.83804178237915, 67.0147659778595, 65.04205560684204]

klog_cost = [361.6074314990966, 371.42134245673464, 355.3634340293695, 374.82732789432765, 366.09103591921905, 361.5195445224251, 363.25919095787486, 368.31776343189114, 362.9767393681853, 368.3206907478954]
klog_time = [69.78836154937744, 64.59479260444641, 68.33480024337769, 66.9317102432251, 68.45734000205994, 70.57396912574768, 67.41261959075928, 66.438485622406, 60.95861220359802, 66.71795439720154]

costs = np.array([k2_cost, k3_cost, k5_cost, k10_cost, klog_cost])
times = np.array([k2_time, k3_time, k5_time, k10_time, klog_time])

average_costs = np.array([avg(cost) for cost in costs])
average_times = np.array([avg(time) for time in times])

print(f"average costs = {average_costs}")
print(f"average times = {average_times}")

#create cumulative distribution function

time_steps = np.linspace(50,90,50)

stats_time_number_successes = []

for item in times:
    count = 0
    sub_array = []
    for i in range(50):
        for time_to_success in item:
            if time_to_success <= time_steps[i]:
                count += 1
        sub_array.append(count/10)
        count = 0
    stats_time_number_successes.append(sub_array)

plt.plot(time_steps, stats_time_number_successes[0])
plt.plot(time_steps, stats_time_number_successes[1])
plt.plot(time_steps, stats_time_number_successes[2])
plt.plot(time_steps, stats_time_number_successes[3])
plt.plot(time_steps, stats_time_number_successes[4])

plt.legend(['k = 2', 'k = 3', 'k = 5', 'k = 10', 'k = O(log(n))'])
plt.xlabel('time [s]')
plt.ylabel('success fraction')

plt.show()