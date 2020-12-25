#!/usr/bin/env python3.9

import sys
import re
import itertools
import functools


def read_file(filename: str, sep: str = '\n') -> list[str]:
    with open(filename, 'rt') as f:
        data = f.read().split(sep)
        return [int(d) for d in data]


def loop(v: int, sn: int):
    v = v * sn
    v = v % 20201227
    return v


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(f'Usage: {sys.argv[0]}  <input>')
        exit(-1)

    data = read_file(sys.argv[1])
    card_pk, door_pk = (data[0], data[1])
    print("--- Challenge 1 ---")
    v = 1
    
    # get loop size
    i = 1
    while True:
        v = loop(v, 7)
        if (v == card_pk):
            break
        i += 1

    key = 1
    for _ in range(i):
        key = loop(key, door_pk)

    print(f"The secret key is {key}")