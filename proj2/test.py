#!/usr/bin/python3

"""
CS-UY 2214
Jeff Epstein
Starter code for E20 simulator
sim.py
"""

from collections import namedtuple
import re
import argparse
import sys
import json

# gridappsd-python module
from gridappsd import GridAPPSD
from gridappsd.simulation import Simulation

# global variables
gapps = None
appName = None
sim_id = None
feeder_mrid = None


def _main():
    global appName, sim_id, feeder_mrid, gapps

    if len(sys.argv)<2 or '-help' in sys.argv:
        usestr =  '\nUsage: ' + sys.argv[0] + ' #nodes\n'
        usestr += '''
Optional command line arguments:
        -help: show this usage message
        '''
        print(usestr, file=sys.stderr, flush=True)
        exit()

    appName = sys.argv[0]

    sim_config_file = './sim_starter/' + sys.argv[1] + '-config.json'
    gapps = GridAPPSD()

    with open(sim_config_file) as config_fp:
        sim_config = json.load(config_fp)

    # if there is a sys.argv[2] command line argument, that indicates not to start a simulation
    if len(sys.argv)<3:
        print('SIM_STARTER initializing simulation from: ' + sim_config_file, file=sys.stderr, flush=True)
        sim = Simulation(gapps, sim_config)
        print('SIM_STARTER about to start simulation...', file=sys.stderr, flush=True)
        sim.start_simulation()
        sim_id = sim.simulation_id
        print('SIM_STARTER simulation started with id: ' + sim_id, file=sys.stderr, flush=True)
        print(sim_id, flush=True)

    # need to dump sim_config before passing it on to downstream modules
    # in order to convert single quotes to double quotes
    sim_req = json.dumps(sim_config)
    print(sim_req, flush=True)

    gapps.disconnect()


if __name__ == '__main__':
    _main()
