#!/usr/bin/env python3

import sys

def read_file(filename: str, sep: str = '\n') -> list[str]:
    with open(filename, 'rt') as f:
        data = f.read().split(sep)
        return data

def slide(l: list[str], right: int = 3, down: int = 1) -> int:
    i: int = down
    j: int = 0
    height: int = len(l)
    width: int = len(l[0])
    num_trees: int = 0
    while i < height:
        j = (j + right) % width
        if l[i][j] == '#':
            num_trees += 1
        i += down
    return num_trees


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(f'Usage: {sys.argv[0]}  <input>')
        exit(-1)

    data: list[str] = read_file(sys.argv[1])
    num_trees: int = slide(data)

    print("======= Solution 1 =======")
    print(f'Number of Trees hit: {num_trees}')

    print("======= Solution 2 =======")
    configs = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    
    product_trees = 1
    for config in configs:
        product_trees *= slide(data, *config)
    print(f'Product of Trees hit: {product_trees}')
    