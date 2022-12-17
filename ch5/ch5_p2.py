import numpy as np
import re

CRATE_LENGTH = 3

class Stack:
    def __init__(self, elems=[]):
        self.elems = elems

    def add(self, e):
        self.elems.append(e)

    def pop(self):
        return self.elems.pop()

    def __repr__(self) -> str:
        return str(self.elems)

def get_crate_line(line):
    crate_line = []
    for i in range(len(line)):
        if i % (CRATE_LENGTH + 1) == 0:
            crate = line[i:i+CRATE_LENGTH].strip()
            crate_line.append(crate)
    return crate_line

def get_crates(f):
    line = f.readline()
    line_lenght = len(line)
    crates = []

    while len(line) == line_lenght:
        crate_line = get_crate_line(line)
        line = f.readline()

        if len(line) == line_lenght:
            crates.append(crate_line)

    return np.array(crates).T.tolist()

def get_stacks(f):
    crates = get_crates(f)

    stacks = []

    for crate_stack in crates:
        stacks.append(Stack(list(filter(lambda x: x != '', crate_stack[::-1]))))

    return stacks

def get_instructions(f):
    instructions_list = []

    line = f.readline()
    while line:
        instructions = re.findall('[0-9]+', line)
        instructions = list(map(int, instructions))
        instructions_list.append(instructions)
        line = f.readline()

    return instructions_list

def operate(stacks, instruction):
    crates = [''] * instruction[0]
    for i in range(instruction[0]):
        crates[-1 * (i+1)] = stacks[instruction[1] - 1].pop()
    for crate in crates:
        stacks[instruction[2] - 1].add(crate)

with open('input') as f:
    
    stacks = get_stacks(f)

    instructions_list = get_instructions(f)

    for instruction in instructions_list:
        operate(stacks, instruction)

    for stack in stacks:
        print(re.findall('[a-zA-Z]+', stack.pop())[0], sep='', end='')
    print()

