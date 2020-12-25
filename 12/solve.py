#!/usr/bin/env python3.9

import sys
import re
import itertools
import functools

def read_file(filename: str, sep: str = '\n') -> list[str]:
    with open(filename, 'rt') as f:
        data = f.read().split(sep)
        return [(d[0], int(d[1:])) for d in data]


def change_dir(op: str, d: str, degree: int):
    directions = list("NESW")
    idx = directions.index(d)
    if op == 'R':
        new_idx = (degree//90 + idx) % 4
    elif op == 'L':
        new_idx = ((-degree)//90 + idx) % 4
    return directions[new_idx]

def nav_norm(op: str, val: int, d: str, x:int, y:int) -> tuple[int,int,str]:
    if op == 'N':
        y += val
    elif op == 'E':
        x += val
    elif op == 'W':
        x -= val
    elif op == 'S':
        y -= val
    elif op == 'F':
        return nav_norm(d, val, d, x, y)
    elif op == 'R' or op == 'L':
        new_d = change_dir(op, d, val)
        return (x, y, new_d)
    return (x, y, d)


def navigate(directions: list[tuple[str, str]]) -> tuple[int, int]:
    x, y = (0, 0)
    d = 'E'
    for direction in directions:
        op, val = direction
        x, y, d = nav_norm(op, val, d, x, y)
    return (x, y)


def manhattan_distance(x: int, y: int) -> int:
    return abs(x) + abs(y)

def navigate_waypoint(directions: list[tuple[str, str]]) -> tuple[int, int]:
    x, y = (0, 0)
    wx, wy = (10, 1)
    d = 'E'
    for direction in directions:
        op, val = direction
        if op in 'NSEW':
            wx, wy, _ = nav_norm(op, val, d, wx, wy)
        else:
            x, y, wx, wy = nav_waypoint(op, val, x, y, wx, wy)
    return (x, y)


def nav_waypoint_rl(op:str, degree:int, wx:int, wy:int) -> tuple[int, int]:
    transformations = [
        lambda x, y: (x, y), # 0 degrees
        lambda x, y: (y, -x), # 90 degrees
        lambda x, y: (-x, -y), # 180 degrees
        lambda x, y: (-y, x), # 270 degrees
    ]
    if op == 'R':
        transformation = transformations[degree//90]
    elif op == 'L':
        transformation = transformations[-degree//90]
    return transformation(wx, wy)


def nav_waypoint(op: str, val: int, x:int, y:int, wx:int, wy:int) -> tuple[int,int, int,int]:
    if op == 'F':
        x += wx * val
        y += wy * val
    elif op == 'R' or op == 'L':
        wx, wy = nav_waypoint_rl(op, val, wx, wy)
    return (x, y, wx, wy)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(f'Usage: {sys.argv[0]}  <input>')
        exit(-1)

    data = read_file(sys.argv[1])
    
    print("--- Challenge 1 ---")
    x, y = navigate(data)
    print(f"Final location manhattan distance: {manhattan_distance(x, y)}")
    
    print("--- Challenge 2 ---")
    x, y = navigate_waypoint(data)
    print(f"Final location manhattan distance: {manhattan_distance(x, y)}")
