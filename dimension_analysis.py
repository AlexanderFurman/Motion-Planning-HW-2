from matplotlib import pyplot as plt
import numpy as np

def fraction_of_volume(dist_from_surface, dimension):
    R = 1

    fraction_volume = (R**dimension - (R-dist_from_surface)**dimension)/R**dimension

    return fraction_volume*100


dist_from_surface = [0.2, 0.1, 0.01]
dimension = range(2, 11)
frac = []

for epsilon in dist_from_surface:
    sub_frac = [fraction_of_volume(epsilon, d) for d in dimension]
    frac.append(sub_frac)

for i in range(len(dist_from_surface)):
    plt.plot(dimension, frac[i], color = 'green')
    plt.plot(dimension, frac[i], '.', color = "red")
    plt.xlabel("Dimension")
    plt.ylabel("Volume [%]")
    # plt.title(f"Fraction of volume when $\epsilon = ${dist_from_surface[i]}, over the dimension number")
    plt.grid()
    plt.savefig(f'dimension-{i}.png')
    plt.show()




