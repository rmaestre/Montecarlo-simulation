"""
This script approximate PI value using Monte Carlo algorithm
"""
from pylab import *
from random import random
import math
import time

# Interactive mode on
ion()
# Sampling
samples = 1000000
# Jumps to print
jumps = 500
# Hits and sample counter
hits = 1
iteration = 1
# List to save points in each iteration
p_hits = []
p_fails = []

# Start sampling
for i in range (1, samples):
    # Get random point getting from a Uniform
    point = [random(), random()]
    # Pi aproximate vale
    pi_approximation = 4 * (hits / iteration)
    # Check if point is into circle
    if math.sqrt(math.pow(point[0], 2) + math.pow(point[1], 2)) <= 1.0:
        hits = hits + 1.0
        # Append point like a hit
        p_hits.append(point)
    else:
        # Append point like a fail
        p_fails.append(point)
    # Plot option
    if iteration % jumps == 0:
        # Print hits and fails points
        scatter(*zip(*p_hits), color='red')
        scatter(*zip(*p_fails), color='blue')
        xlabel("Montecarlo Simulation to aproximate PI value")
        # Draw plot
        draw()
        # Clean points draed
        p_hits = []
        p_fails = []
        time.sleep(0.5)
    # Debug info
    print "Pi= %0.10f (%0.5f error) (%0.4f%% hits) Sample: %d" % (pi_approximation, 
                                            math.fabs(pi_approximation - math.pi), 
                                            ((hits*100)/iteration), 
                                            iteration)
    # Incement sample
    iteration += 1