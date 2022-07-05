from random import random
from threading import Thread
import numpy as np

AREA = 200
NUM_SEEDS = 3

voronoi = np.zeros(AREA, AREA, np.int32)
seeds = np.array(NUM_SEEDS, 2)

for seed in NUM_SEEDS:
    seeds[seed, 1] = random.randrange(1, AREA,3)
    seeds[seed, 2] = random.randrange(1, AREA,3)


