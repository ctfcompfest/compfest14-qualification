#!/usr/bin/env python3
# Greedy BFS solver for The Maze Jogger by sl0ck
# May not be optimized because mager :u

from pwn import *
from queue import PriorityQueue

p = process("./maze.py")

inverse = {1: 2, 2: 1, 3: 4, 4: 3}
direction_to_cardinal = {1: 2, 2: 4, 3: 3, 4: 1}
cardinal_to_direction = {1: 4, 2: 1, 3: 3, 4: 2}

cell_map = dict()
origin_to_cell_path = dict()
node_queue = PriorityQueue()

class Cell():
    def __init__(self, pos, dist):
        self.pos = pos
        self.dist = dist
        self.neighbors = [None, None, None, None] # N E S W
        self.visited = False
        self.origin = False
        self.path_to_origin = []
    
    def __repr__(self):
        return f"Cell at {self.pos}, origin: {self.origin}, distance to goal: {self.dist}"
        
    def __lt__(self, other):
        return self.dist <= other.dist

def get_cell():
    res = p.recvuntil(b"Position: ")
    if b"Wowie" in res:
        print(res)
        exit()
    
    if b"Can't move" in res: # If that direction is a wall
        return False
    
    pos = p.recvline().rstrip()
    
    if pos in cell_map:
        return cell_map[pos]

    p.recvuntil(b"Distance from prize: ")
    dist = float(p.recvline().rstrip().decode())
    
    return Cell(pos, dist)
    
def explore(cell):
    for i in range(1, 5):
        p.recvuntil(b">>> ")
        p.sendline(str(i).encode())
        curr_cell = get_cell()
        if curr_cell != False and curr_cell.visited:
            p.recvuntil(b">>> ")
            p.sendline(str(inverse[i]).encode())
            
        if curr_cell != False and not curr_cell.visited:
            p.recvuntil(b">>> ")
            p.sendline(str(inverse[i]).encode())
            curr_cell.neighbors[direction_to_cardinal[inverse[i]] - 1] = cell
            
            potential_path_to_origin = [str(inverse[i]).encode()] + cell.path_to_origin
            if not curr_cell.path_to_origin or len(potential_path_to_origin) < len(curr_cell.path_to_origin):
                curr_cell.path_to_origin = potential_path_to_origin
            
            potential_path_to_cell = origin_to_cell_path[cell.pos] + [str(i).encode()]
            if not curr_cell.pos in origin_to_cell_path or len(potential_path_to_cell) < len(origin_to_cell_path[curr_cell.pos]):
                origin_to_cell_path[curr_cell.pos] = potential_path_to_cell
            
            if not curr_cell.pos in cell_map:
                cell_map[curr_cell.pos] = curr_cell
                
            if not any(curr_cell.pos == el.pos for el in node_queue.queue):
                node_queue.put(curr_cell, curr_cell.dist)
        
        cell.neighbors[direction_to_cardinal[i] - 1] = curr_cell
        cell.visited = True

origin_cell = get_cell()
origin_cell.visited = True
origin_cell.origin = True
cell_map[origin_cell.pos] = origin_cell
origin_to_cell_path[origin_cell.pos] = []
explore(origin_cell)

curr_cell = origin_cell

while True:
    if curr_cell.origin:
        curr_cell = node_queue.get() # Get the next closest cell
        for move in origin_to_cell_path[curr_cell.pos]:
            p.recvuntil(b">>> ")
            p.sendline(move)
        explore(curr_cell)
        
    else:
        for i, cell in enumerate(curr_cell.neighbors):
            if cell != False and not cell.visited and cell.dist <= node_queue.queue[0].dist:
                curr_cell = cell
                h = p.recvuntil(b">>> ")
                p.sendline(str(cardinal_to_direction[i + 1]).encode())
                explore(curr_cell)
        
        for move in curr_cell.path_to_origin:
            h = p.recvuntil(b">>> ")
            p.sendline(move)
            curr_cell = get_cell()