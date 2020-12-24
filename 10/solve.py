#!/usr/bin/env python3.9

import sys
import re
import itertools
import functools

# memoize (rem_adapters, prev_num)
MEMOIZE = {}

def read_file(filename: str, sep: str = '\n') -> list[str]:
    with open(filename, 'rt') as f:
        data = f.read().split(sep)
        return [int(d) for d in data]

def find_chain(rem_adapters: tuple[int], prev_num: int, max_rating: int) -> int:
    idx: int = rem_adapters.index(prev_num)
    rem_adapters = rem_adapters[idx:]
    candidate_adapters = [x for x in rem_adapters if x > prev_num and prev_num + 3 >= x]

    total_count: int = MEMOIZE.get((rem_adapters, prev_num))
    if total_count != None:
        return total_count
    else:
        total_count = 0
        for adapter in candidate_adapters:
            if adapter == max_rating:
                total_count += 1
            else:
                total_count += find_chain(rem_adapters, adapter, max_rating)
        MEMOIZE[(rem_adapters, prev_num)] = total_count
        return total_count

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(f'Usage: {sys.argv[0]}  <input>')
        exit(-1)

    data = read_file(sys.argv[1])
    highest_rating: int = max(data) + 3

    print("--- Challenge 1 ---")
    # data preparation
    data.sort()
    data.insert(0, 0)
    data.append(highest_rating)

    one_jolts: int = 0
    three_jolts: int = 0

    for i, j in zip(range(len(data)-1), range(1, len(data))):
        diff = data[j] - data[i]
        if diff == 1:
            one_jolts += 1
        elif diff == 3:
            three_jolts += 1
    print(f"Number of 1-jolt differences multiplied by the number of 3-jolt differences: {one_jolts * three_jolts}")

    print("--- Challenge 2 ---")
    # remove the 0th entry
    data = data
    print(f"Total number of distinct ways you can arrange the adapters to connect the charging outlet to your device: {find_chain(tuple(data), 0, highest_rating)}")
