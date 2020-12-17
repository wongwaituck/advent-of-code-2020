#!/usr/bin/env python3

import sys
import networkx as nx
import re
import itertools
import functools

def read_file(filename: str, sep: str = '\n') -> list[str]:
    with open(filename, 'rt') as f:
        data = f.read().split(sep)
        return [int(d) for d in data]

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(f'Usage: {sys.argv[0]}  <input>')
        exit(-1)

    data = read_file(sys.argv[1])
    print("--- Challenge 1 ---")
    errno = 0
    PREAMBLE_LEN = 25

    for i in range(PREAMBLE_LEN, len(data)):
        previous_numbers = data[i-PREAMBLE_LEN:i]
        all_prev_sums = [s[0]+s[1] for s in list(itertools.combinations(previous_numbers, 2))]
        if data[i] not in all_prev_sums:
            errno = data[i]
            break

    print(f"First number that does not obey this property: {errno}")

    print("--- Challenge 2 ---")
    for i in range(len(data)):
        for j in range(len(data)):
            if j > i and sum(data[i:j]) == errno:
                sol = min(data[i:j]) + max(data[i:j])
                print(f"Encryption weakness: {sol}")
                exit(0)