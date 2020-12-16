#!/usr/bin/env python3

import sys
import networkx as nx
import re

def read_file(filename: str, sep: str = '\n') -> list[str]:
    with open(filename, 'rt') as f:
        data = f.read().split(sep)
        return data

def process_data_1(l: list[str], g: nx.Graph) -> None:
    for ls in l:
        ls = ls.strip()
        if 'no other' in ls or len(ls) == 0:
            continue
        m = re.search('^([\w ]+) bags contain ((\d+) ([\w ]+) bags?,?) ?((\d+) ([\w ]+) bags?,?)? ?((\d+) ([\w ]+) bags?,?)? ?((\d+) ([\w ]+) bags?,?)?\.$', ls)
        container = m.group(1)
        g.add_node(container)
        try:
            for i in range(3, 14, 3):
                capacity = int(m.group(i))
                contained = m.group(i+1) 
                g.add_node(contained)
                g.add_edge(contained, container, weight=capacity)
        except:
            # hacky way but i can't find number of matches in re :(
            continue


def process_data_2(l: list[str], g: nx.Graph) -> None:
    for ls in l:
        ls = ls.strip()
        if 'no other' in ls or len(ls) == 0:
            continue
        m = re.search('^([\w ]+) bags contain ((\d+) ([\w ]+) bags?,?) ?((\d+) ([\w ]+) bags?,?)? ?((\d+) ([\w ]+) bags?,?)? ?((\d+) ([\w ]+) bags?,?)?\.$', ls)
        container = m.group(1)
        g.add_node(container)
        try:
            for i in range(3, 14, 3):
                capacity = int(m.group(i))
                contained = m.group(i+1) 
                g.add_node(contained)
                g.add_edge(container, contained, weight=capacity)
        except:
            # hacky way but i can't find number of matches in re :(
            continue


def get_contained_bags(n: str, g: nx.Graph) -> int:
    neighbors = list(nx.neighbors(g, n))
    if len(neighbors) == 0:
        return 0
    else:
        s = 0
        for neighbor in neighbors:
            # get edge weight
            fr = n
            to = neighbor
            edge_weight = g.get_edge_data(fr, to)['weight']

            # get bags that the bag type can contain, plus the number of bags of that type
            s += edge_weight * (get_contained_bags(to, g) + 1)
        return s

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(f'Usage: {sys.argv[0]}  <input>')
        exit(-1)

    # create graph where the contained bag type points to the container
    # then we simply have to grab the descednants to get all possible bag types
    g1 = nx.DiGraph()
    data: list[str] = read_file(sys.argv[1])
    cn = 'shiny gold'
    process_data_1(data, g1)

    print("--- Challenge 1 ---")
    print(f"Number of bag types that can contain a shiny gold bag: {len(nx.descendants(g1, cn))}")

    # create graph where the container bag type points to the contained
    # we then do a DFS to get number of bags that each bag type can contain
    g2 = nx.DiGraph()
    process_data_2(data, g2)

    print("--- Challenge 2 ---")
    print(f"Shiny gold bags must contain {get_contained_bags(cn, g2)}")