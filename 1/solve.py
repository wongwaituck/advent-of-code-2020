#!/usr/bin/env python3

import sys

def read_file(filename: str, sep: str = '\n') -> list[str]:
    with open(filename, 'rt') as f:
        data = f.read().split(sep)
        return data

def find_2sum(l: list[int], target: int = 2020) -> tuple[int, int]:
    # use the dictionary method which is O(n), see: https://web.stanford.edu/class/cs9/sample_probs/TwoSum.pdf
    lookup: dict[int, int] = {}

    for li in l:
        if lookup.get(target-li) == None:
            lookup[li] = 1
        else:
            return li, target-li

    return 0, 0


def find_3sum(l: list[int], target: int = 2020) -> tuple[int, int, int]:
    # same dictionary method, quadratic
    lookup: dict[int, int] = {}
    for li in l:
        lookup[li] = 1
    
    for li in l:
        for lj in l:
            lk: int = target - li - lj 
            if lookup.get(lk) != None:
                return li, lj, target - li -lj

    return 0, 0, 0


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(f'Usage: {sys.argv[0]}  <input>')
        exit(-1)

    data: list[str] = read_file(sys.argv[1])
    data_ints: list[int] = list(map(int, data))
    x, y = find_2sum(data_ints)
    print("======= 2 SUM =======")
    print(f'Entries that sum to 2020: {x}, {y}')
    print(f'Product: {x * y}')

    x, y, z = find_3sum(data_ints)
    print("======= 3 SUM =======")
    print(f'Entries that sum to 2020: {x}, {y}, {z}')
    print(f'Product: {x * y * z}')