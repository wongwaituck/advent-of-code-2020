#!/usr/bin/env python3

import sys
from functools import reduce

def read_file(filename: str, sep: str = '\n') -> list[str]:
    with open(filename, 'rt') as f:
        data = f.read().split(sep)
        return data


def process_data(s: str) -> tuple[int, int, str, str]:
    kv = [v.strip() for v in s.split(':')]
    key, val = kv[0].strip(), kv[1].strip()
    idx_c = key.split(' ')
    idxs, c = idx_c[0], idx_c[1]
    idxs = [int(idx) for idx in idxs.split('-')]
    return idxs[0], idxs[1], c, val


def check_policy1(lo: int, hi: int, c: str, pw: str) -> bool:
    num_c = len(pw.split(c)) - 1
    if num_c >= lo and num_c <= hi:
        return True
    else:
        return False


def check_policy2(lo: int, hi: int, c: str, pw: str) -> int:
    l_pw = len(pw) 
    crit_1: int = 1 if lo <= l_pw and pw[lo-1] == c else 0
    crit_2: int = 1 if hi <= l_pw and pw[hi-1] == c else 0
    return crit_1 ^ crit_2


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(f'Usage: {sys.argv[0]}  <input>')
        exit(-1)

    data: list[str] = read_file(sys.argv[1])
    processed_data: tuple[int, int, str, str] = list(map(process_data, data)) 
    
    count1: int = reduce(lambda x, y: x + y, map(lambda x: 1 if x else 0, [check_policy1(*v) for v in processed_data]))
    print(f"Problem 1: Total password wins {count1}")

    count2: int = reduce(lambda x, y: x + y, [check_policy2(*v) for v in processed_data])
    print(f"Problem 2: Total password wins {count2}")