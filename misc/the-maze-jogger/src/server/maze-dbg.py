#!/usr/bin/env python3
import random
import math

WIDTH = 5
HEIGHT = WIDTH

class Maze():
    def __init__(self, width, height):
        self.maze = []
        for i in range(height):
            cols = []
            for j in range(width):
                cols.append(None)
            self.maze.append(cols)
        
    def __repr__(self):
        return f"{self.maze}"

class Cell():
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.walls = [0, 0, 0, 0] # N E S W
        self.visited = False
        
    def __repr__(self):
        return f"({self.row}, {self.col}) Walls: {self.walls}"

class Player():
    def __init__(self, maze, cell):
        self.maze = maze
        self.cell = cell
        
    def move_forward(self):
        if self.cell.walls[1] == 0:
            self.cell = self.maze.maze[self.cell.row][self.cell.col + 1]
            return True
        return False
        
    def move_backward(self):
        if self.cell.walls[3] == 0:
            self.cell = self.maze.maze[self.cell.row][self.cell.col - 1]
            return True
        return False
        
    def move_right(self):
        if self.cell.walls[2] == 0:
            self.cell = self.maze.maze[self.cell.row + 1][self.cell.col]
            return True
        return False
        
    def move_left(self):
        if self.cell.walls[0] == 0:
            self.cell = self.maze.maze[self.cell.row - 1][self.cell.col]
            return True
        return False

def init_maze(maze):
    for i in range(WIDTH):
        for j in range(HEIGHT):
            maze.maze[i][j] = Cell(i, j)
    maze.maze[0][0].walls = [1, 0, 0, 1]
    maze.maze[1][0].walls = [0, 0, 0, 1]
     
def main():
    print("Generating maze.....")
    maze = Maze(WIDTH, HEIGHT)
    init_maze(maze)
    winning_cell = maze.maze[4][4]
    
    print("Initializing player.....\n")
    player = Player(maze, maze.maze[0][0])
    print("Welcome to maze!")
    while True:
        if player.cell == winning_cell:
            print("YOU WON!!!!")
            print(f"Final Position: ({player.cell.row} {player.cell.col})")
            return
        dist = math.sqrt(pow(max(winning_cell.row, player.cell.row) - min(winning_cell.row, player.cell.row), 2) + pow(max(winning_cell.col, player.cell.col) - min(winning_cell.col, player.cell.col), 2)) 
        print(f"Position: ({player.cell.row} {player.cell.col})")
        print(f"Distance from prize: {dist}")
        inp = input("What do you wanna do?\n1) Move forward\n2) Move backward\n3) Move right\n4) Move left\n5) Surrender\n>>> ")
        if inp == '1':
            if player.move_forward():
                print("Moved forward.")
            else:
                print("Can't move forward.")
        elif inp == '2':
            if player.move_backward():
                print("Moved backward.")
            else:
                print("Can't move backward.")
        elif inp == '3':
            if player.move_right():
                print("Moved right.")
            else:
                print("Can't move right.")
        elif inp == '4':
            if player.move_left():
                print("Moved left.")
            else:
                print("Can't move left.")
        elif inp == '5':
            print("Thou hast been vanquished!")
            return
        else:
            print("What are you doing broo")
        print()
    
if __name__ == "__main__":
    exit(main())
