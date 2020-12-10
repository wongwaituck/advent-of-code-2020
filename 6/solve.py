#!/usr/bin/env python3

import sys


def read_file(filename: str, sep: str = '\n') -> list[str]:
    with open(filename, 'rt') as f:
        data = f.read().split(sep)
        return data


def sum_lengths(l: list[set[str]]) -> int:
    return sum(map(len, l))


def challenge1(l: list[str]) -> list[set[str]]:
    i = 0
    sz_l = len(l)
    out = []
    while i < sz_l:
        current_group: set[str] = set([])
        while i < sz_l and len(l[i]) != 0:
            chars = set([c for c in l[i]])
            current_group = current_group.union(chars)
            i += 1
        out.append(current_group)
        i += 1
    return out

def challenge2(l: list[str]) -> list[set[str]]:
    i = 0
    sz_l = len(l)
    out = []
    while i < sz_l:
        current_group: set[str] = set([chr(c + ord('a')) for c in range(26)])
        while i < sz_l and len(l[i]) != 0:
            chars = set([c for c in l[i]])
            current_group = current_group.intersection(chars)
            i += 1
        out.append(current_group)
        i += 1
    return out

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(f'Usage: {sys.argv[0]}  <input>')
        exit(-1)

    print("--- Challenge 1 ---")
    data: list[str] = read_file(sys.argv[1])
    processed_data : list[set[str]] = challenge1(data)
    print(f"Sum of counts for union: {sum_lengths(processed_data)}")

    print("--- Challenge 2 ---")
    processed_data2 : list[set[str]] = challenge2(data)
    print(f"Sum of counts for intersection: {sum_lengths(processed_data2)}")