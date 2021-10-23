# E_20

# E_20 compiler

### Introduction

**This project represents a substantive programming exercise. ***. Read the provided E20assembly language examples.**

### Specifications

Your task is to write an E20 simulator: a program that will execute E20 machine language. Normally,machine language would be executed by a processor, but for simplicity, we will reproduce the behavior of anE20 processor in software. A correct simulator is one that will produce identical results to those producedby a real E20 processor, as described in the E20 manual.Each E20 machine language program is a sequence of commands to be interpreted by an E20 processor,or a simulation thereof. Your simulator will need to accurately reproduce the state that is manipulated bythose commands: the program counter, the general-purpose registers, and memory.For example, consider the machine language instruction0010100010000011. This machine languageinstruction corresponds to the assembly language instructionaddi $1, $2, 3. Therefore, in order to executethis instruction, we must first know the current value of register$2. We add3to that value, and store thesum in register$1. This new value may then be accessed by subsequent instructions.The basic operation of your simulator is as follows:

1.Initialize the processor state, including the program counter, the general-purpose registers, and memory.

2.Examine the instruction pointed to by the program counter. Determine what action is to be taken.

3.Take the indicated action, updating the value of the program counter, the general-purpose registers,and memory appropriately.

4.If the executed instruction is ahaltinstruction, end the simulation.

5.Otherwise, go to step 2.

For the purposes of this simulation, the initial state of the program counter is zero, and the initial stateof all registers is zero. The machine code program will be loaded into memory starting at address zero, andthe value of all other memory cells is zero.

### Input

The input to your simulator will be the name of an E20 machine language file, given on the command line.By convention, E20 machine language files have an.binsuﬀix.Your program will read in the contents of the file. 

You may assume that the file contains well-formedE20 machine language code. The file may contains comments, which your program should ignore.1

## Output

Your program should print to stdout the final state of the simulated E20 processor, at the point when thesimulation halts. Specifically, your program should print out the final value of the program counter (inunsigned decimal) and the eight general-purpose registers (in unsigned decimal). In addition, your programshould print out the value of the first 128 memory cells (in hex).Below is an example invocation of a simulator from Linux’sbash. In this case, we are simulating theexecution of the machine language program given above
