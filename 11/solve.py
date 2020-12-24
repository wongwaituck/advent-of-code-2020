#!/usr/bin/env python3.9

import sys
import re
import itertools
import functools

def read_file(filename: str, sep: str = '\n') -> list[list[str]]:
    with open(filename, 'rt') as f:
        data = f.read().split(sep)
        return [list(d) for d in data if d]

def get_adjacent_cells(board: list[list[str]], row: int, col: int) -> list[str]:
    min_row: int = row - 1 if row > 0 else row
    min_col: int = col - 1 if col > 0 else col
    max_row: int = row + 1 if row < len(board) - 1 else row
    max_col: int = col + 1 if col < len(board[0]) - 1 else col

    cells: list[str] = [board[i][j] for i in range(min_row, max_row + 1) for j in range(min_col, max_col + 1)]
    cells.remove(board[row][col])
    return cells

def simulate_board(board: list[list[str]], adj_func: callable = get_adjacent_cells, threshold: int = 4) -> list[list[str]]:
    output_board = [['.' for _ in range(len(board[0]))] for _ in range(len(board))]

    for i in range(len(board)):
        row = board[i]
        for j in range(len(row)):
            cell: str = board[i][j]
            adj_cells: list[str] = adj_func(board, i, j)
            if cell == 'L' and '#' not in adj_cells:
                # cell is empty and there are no occupied seats adjacent to it, the seat becomes occupied.
                output_board[i][j] = '#'
            elif cell == '#' and adj_cells.count('#') >= threshold:
                # cell is occupied and four or more seats adjacent to it are also occupied, the seat becomes empty
                output_board[i][j] = 'L'
            else:
                output_board[i][j] = cell
    return output_board


def in_bounds(board: list[list[str]], row: int, col: int):
    if row < 0 or col < 0:
        return False
    elif row >= len(board) or col >= len(board[0]):
        return False
    else:
        return True


def find_visible_seat(board: list[list[str]], row: int, col: int, incr_func: callable):
    row_p, col_p = incr_func(row, col)
    while in_bounds(board, row_p, col_p):
        cell = board[row_p][col_p]
        if cell == 'L' or cell == '#':
            return cell
        else:
            row_p, col_p = incr_func(row_p, col_p)
    return '.'


def get_visible_cells(board: list[list[str]], row: int, col: int) -> list[str]:
    finders = [
        lambda x, y: (x+1, y),
        lambda x, y: (x-1, y),
        lambda x, y: (x, y+1),
        lambda x, y: (x, y-1),
        lambda x, y: (x+1, y+1),
        lambda x, y: (x-1, y-1),
        lambda x, y: (x-1, y+1),
        lambda x, y: (x+1, y-1),
    ]

    cells: list[str] = [find_visible_seat(board, row, col, f) for f in finders]
    return cells


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(f'Usage: {sys.argv[0]}  <input>')
        exit(-1)

    board = read_file(sys.argv[1])
    org_board = board

    print("--- Challenge 1 ---")
    next_board = simulate_board(board)
    while board != next_board:
        board = next_board
        next_board = simulate_board(board)
    sum_occupied: int = sum(map(lambda y: sum(map(lambda x: 1 if x == '#' else 0, y)), board))
    print(f"Seats occupied: {sum_occupied}")

    print("--- Challenge 2 ---")
    board = org_board
    next_board = simulate_board(board, get_visible_cells, threshold=5)
    while board != next_board:
        board = next_board
        next_board = simulate_board(board, get_visible_cells, threshold=5)
    sum_occupied: int = sum(map(lambda y: sum(map(lambda x: 1 if x == '#' else 0, y)), board))
    print(f"Seats occupied: {sum_occupied}")
