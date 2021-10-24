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

# Some helpful constant values that we'll be using.
Constants = namedtuple("Constants",["NUM_REGS", "MEM_SIZE", "REG_SIZE"])
constants = Constants(NUM_REGS = 8, 
                      MEM_SIZE = 2**13,
                      REG_SIZE = 2**16)

def load_machine_code(machine_code, mem):
    """
    Loads an E20 machine code file into the list
    provided by mem. We assume that mem is
    large enough to hold the values in the machine
    code file.
    sig: list(str) -> list(int) -> NoneType
    """
    machine_code_re = re.compile("^ram\[(\d+)\] = 16'b(\d+);.*$")
    expectedaddr = 0
    for line in machine_code:
        match = machine_code_re.match(line)
        if not match:
            raise ValueError("Can't parse line: %s" % line)
        addr, instr = match.groups()
        addr = int(addr,10)
        instr = int(instr,2)
        if addr != expectedaddr:
            raise ValueError("Memory addresses encountered out of sequence: %s" % addr)
        if addr >= len(mem):
            raise ValueError("Program too big for memory")
        expectedaddr += 1
        mem[addr] = instr

def print_state(pc, regs, memory, memquantity):
    """
    Prints the current state of the simulator, including
    the current program counter, the current register values,
    and the first memquantity elements of memory.
    sig: int -> list(int) -> list(int) - int -> NoneType
    """
    print("Final state:")
    print("\tpc="+format(pc,"5d"))
    for reg, regval in enumerate(regs):
        print(("\t$%s=" % reg)+format(regval,"5d"))
    line = ""
    for count in range(memquantity):
        line += format(memory[count], "04x")+ " "
        if count % 8 == 7:
            print(line)
            line = ""
    if line != "":
        print(line)

def main():
    parser = argparse.ArgumentParser(description='Simulate E20 machine')
    parser.add_argument('filename', help='The file containing machine code, typically with .bin suffix')
    cmdline = parser.parse_args()

    with open(cmdline.filename) as file:
        pass # TODO: your code here. Load file and parse using load_machine_code

    # TODO: your code here. Do simulation.

    # TODO: your code here. print the final state of the simulator before ending, using print_state
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

if __name__ == "__main__":
    main()
#ra0Eequ6ucie6Jei0koh6phishohm9