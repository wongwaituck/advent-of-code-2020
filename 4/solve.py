#!/usr/bin/env python3

import sys
import re

def read_file(filename: str, sep: str = '\n') -> list[str]:
    with open(filename, 'rt') as f:
        data = f.read().split(sep)
        return data


def check_passport1(d: dict) -> bool:
    necessary_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for field in necessary_fields:
        if d.get(field) == None:
            return False
    return True

def check_passport2(d: dict) -> bool:
    necessary_fields = {
        'byr': "^(19[2-9]\d)|(200[0-2])$", 
        'iyr': "^(20[1]\d)|(2020)$", 
        'eyr': "^(202\d)|(2030)$", 
        'hgt': "^(1[5-8]\dcm)|(19[0-3]cm)|(59in)|(6\din)|(7[0-6]in)$", 
        'hcl': "^#[0-9a-f]{6}$" , 
        'ecl': "^(amb|blu|brn|gry|grn|hzl|oth)$", 
        'pid': "^[0-9]{9}$"
    }
    for field in necessary_fields.keys():
        if d.get(field) == None:
            return False
        if re.match(necessary_fields[field], d[field]) == None:
            return False
   
    return True

def process_line(s: str, d: dict) -> dict:
    kvs = s.split(' ')
    kv_pairs = [kv.strip().split(':') for kv in kvs]
    for kv_pair in kv_pairs:
        k, v = kv_pair
        d[k.strip()] = v.strip()
    return d

def process_data(l: list[str], check: callable) -> int:
    good_passports = 0
    i = 0
    while i < len(l): 
        passport = {}
        ls = l[i]
        while len(ls) != 0:
            process_line(ls, passport)
            i += 1
            if i >= len(l):
                break
            ls = l[i]
        if check(passport):
            good_passports += 1
        i += 1
    return good_passports
    

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(f'Usage: {sys.argv[0]}  <input>')
        exit(-1)

    print("--- Challenge 1 ---")
    data: list[str] = read_file(sys.argv[1])
    print(f"Total good passports: {process_data(data, check_passport1)}")

    print("--- Challenge 2 ---")
    print(f"Total good passports: {process_data(data, check_passport2)}")
