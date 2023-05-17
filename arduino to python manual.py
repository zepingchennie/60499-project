#arduino to python
from itertools import count
import numpy as np
import pyfirmata
import time
import matplotlib
from matplotlib import pyplot as plt
board = pyfirmata.Arduino('COM3')
it = pyfirmata.util.Iterator(board)
it.start()

#step times (sec)
adsorption_delay=15
depressurization_delay=4.5
purge_delay=5.5

#o2 purity conversion
conversion=100*5/4

#board pin setup 
analog_input=board.get_pin('a:0:i')
sieve_valve=board.get_pin('d:4:o')
purge_valve=board.get_pin('d:7:o')

#counter
total_cycle=3
cycle=1
run=1

#data generation
while True:
    while cycle<total_cycle:
        print("Current Cycle", end=" ")
        print(cycle)
        # pressurization + adsorption
        sieve_valve.write(1)
        purge_valve.write(1)
        time.sleep(adsorption_delay)
        purity=conversion*analog_input.read()
        print("adsorption", end=" ")
        print(purity)
        
        #depressurization
        sieve_valve.write(0)
        purge_valve.write(1)
        time.sleep(depressurization_delay)
        purity=conversion*analog_input.read()
        print("depressurization", end=" ")
        print(purity)
        
        #purge
        sieve_valve.write(0)
        purge_valve.write(0)
        time.sleep(purge_delay)
        purity=conversion*analog_input.read()
        print("Purge", end=" ")
        print(purity)
        #counter
        cycle=cycle+1
    
    #resets cycle
    cycle=1
    run=run+1