#!/usr/bin/env python3

import sys
import networkx as nx
import re

def read_file(filename: str, sep: str = '\n') -> list[str]:
    with open(filename, 'rt') as f:
        data = f.read().split(sep)
        return data


class Instruction:
    def __init__(self, instr: str, arg: int):
        self.instr = instr
        self.arg = int(arg)


# returns (pc, acc)
def exec(instrs: list[Instruction], pc: int, accumulator: int) -> tuple[int, int]:
    instr: Instruction = instrs[pc]
    if instr.instr == 'nop':
        return pc + 1, accumulator
    elif instr.instr == 'acc':
        return pc + 1, accumulator + instr.arg
    elif instr.instr == 'jmp':
        return pc + instr.arg, accumulator
    else:
        print(f'Wrong instruction... {instr.instr}')
        assert(False)


def get_instrs(l: list[str]) -> list[Instruction]:
    splitted = [ls.split() for ls in l]
    return [Instruction(ls[0], ls[1]) for ls in splitted]

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(f'Usage: {sys.argv[0]}  <input>')
        exit(-1)

    data = read_file(sys.argv[1])
    instrs = get_instrs(data)

    print("--- Challenge 1 ---")
    accumulator = 0
    pc = 0
    executed_instrs = set([])
    
    while instrs[pc] not in executed_instrs:
        executed_instrs.add(instrs[pc])
        pc, accumulator = exec(instrs, pc, accumulator)

    print(f"Accumulator value: {accumulator}")

    print("--- Challenge 2 ---")
    final_accumulator = 0
    for i, instr in enumerate(instrs):
        if instr.instr == 'nop' or instr.instr == 'jmp':
            old_instr = instr
            instr_op = 'nop' if instr.instr == 'jmp' else 'jmp'
            new_instr = Instruction(instr_op, instr.arg)
            instrs[i] = new_instr
            accumulator = 0
            pc = 0
            executed_instrs = set([])
            while instrs[pc] not in executed_instrs:
                executed_instrs.add(instrs[pc])
                pc, accumulator = exec(instrs, pc, accumulator)
                if (pc == len(instrs)):
                    final_accumulator = accumulator
                    break
            instrs[i] = old_instr
        else:
            # acc instructions are not affected
            pass

    print(f"Proper execution accumulator value: {final_accumulator}")