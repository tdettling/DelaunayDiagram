from random import random
from threading import Thread
import numpy as np
import math

AREA = 200
NUM_SEEDS = 3

voronoi = np.zeros(AREA, AREA, np.int32)
seeds = np.array(NUM_SEEDS, 2)
adjMatrix = np.zeros(NUM_SEEDS, NUM_SEEDS, np.int32) 

for seed in NUM_SEEDS:
    seeds[seed, 1] = random.randrange(1, AREA,3)
    seeds[seed, 2] = random.randrange(1, AREA,3)

for i in AREA:
    for j in AREA:
        shortestDistence = 2147483647
        closestSeed = 0
        for k in NUM_SEEDS:
            distance = sqrt((i - seeds[k,1])^2 + (j - seeds[k,2])^2)
            if distance < shortestDistence:
                shortestDistence = distance
                closestSeed = k
        voronoi[i,j] = closestSeed

#fixme adjacency stuff
