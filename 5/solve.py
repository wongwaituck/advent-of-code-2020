#!/usr/bin/env python3

import sys


NUM_SEATS_PER_ROW = 8
NUM_ROWS = 128


def read_file(filename: str, sep: str = '\n') -> list[str]:
    with open(filename, 'rt') as f:
        data = f.read().split(sep)
        return data


def get_num(s: str, n: list[int], bot_char: str, top_char: str) -> int:
    if len(s) == 0:
        assert len(n) == 1
        return n[0]
    else:
        half_len = len(n) // 2
        if s[0] == bot_char:
            n = n[:half_len]
            return get_num(s[1:], n, bot_char, top_char)
        elif s[0] == top_char:
            n = n[half_len:]
            return get_num(s[1:], n, bot_char, top_char)
        else:
            print(f"Wrong character: {s[0]}")
            assert False

def parse_seat_num(s: str) -> int:
    r = get_num(s[:-3], range(NUM_ROWS),  bot_char='F', top_char='B')
    c = get_num(s[-3:], range(NUM_SEATS_PER_ROW), bot_char='L', top_char='R')
    return r * NUM_SEATS_PER_ROW + c


def challenge1(l: list[str]) -> int:
    return max(map(parse_seat_num, l))


def challenge2(l: list[str]) -> int:
    seat_ids = list(map(parse_seat_num, l))
    seat_ids.sort()
    for seat_id in seat_ids:
        if seat_id + 1 not in seat_ids and seat_id + 2 in seat_ids:
            return seat_id + 1


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(f'Usage: {sys.argv[0]}  <input>')
        exit(-1)

    print("--- Challenge 1 ---")
    data: list[str] = read_file(sys.argv[1])
    print(f"Largest seat ID: {challenge1(data)}")

    print("--- Challenge 2 ---")
    print(f"My Seat ID: {challenge2(data)}")