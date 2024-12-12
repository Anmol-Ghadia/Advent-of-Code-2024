from pathlib import Path 
import numpy as np
from enum import Enum

class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

def read_matrix():
    # read the input file
    with open(Path('given','input.txt'), 'r') as file:
        lines = file.readlines()
    
    # remove newline character
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n','')
        
    # convert the lines into a 2d matrix
    matrix = []
    for line in lines:
        # make sure all rows have same number of elements
        assert len(line) == len(lines[0])
        
        row = []
        for char in line:
            row.append(char)
        matrix.append(row)
    
    matrix = np.array(matrix)
    
    # find the starting position of guard
    # returns (y,x) and Direction
    loc = np.argwhere(matrix=="^")
    if (len(loc) != 0):
        return matrix, tuple(loc[0]), Direction.UP
    loc = np.argwhere(matrix==">")
    if (len(loc) != 0):
        return matrix, tuple(loc[0]), Direction.RIGHT
    loc = np.argwhere(matrix=="v")
    if (len(loc) != 0):
        return matrix, tuple(loc[0]), Direction.DOWN
    loc = np.argwhere(matrix=="<")
    if (len(loc) != 0):
        return matrix, tuple(loc[0]), Direction.LEFT
    
    raise "Unexpected input"

def pretty_print(mat):
    print("="*20)
    for i in range(mat.shape[1]):
        for j in range(mat.shape[0]):
            print(mat[i,j],end="")
        print()
    print("="*20)

# moves once in the given direction from location
def move_once(location, direction):
    dir = [(-1,0),(0,1),(1,0),(0,-1)][direction.value]
    return [location[0] + dir[0], location[1]+ dir[1]]

# returns true if location is within bounds of the matrix
def in_bounds(mat,location):
    if (location[0] < 0 or location[1] < 0):
        return False
    if (mat.shape[0] <= location[0] or mat.shape[1] <= location[1]):
        return False
    return True

def rotate_right(dir):
    if (dir == Direction.UP):
        return Direction.RIGHT
    if (dir == Direction.RIGHT):
        return Direction.DOWN
    if (dir == Direction.DOWN):
        return Direction.LEFT
    if (dir == Direction.LEFT):
        return Direction.UP    
    raise "Unexpected direction"

# iterates through the matrix, and marks the visited locations with X
def mark_path(mat, loc, dir):
    
    while True:
        new_loc = tuple(move_once(loc,dir))
        if (not in_bounds(mat,new_loc)):
            # exiting the matrix
            mat[loc] = "X"
            break
        
        if mat[new_loc] == "#":
            # hit a barrier
            dir = rotate_right(dir)
            continue
        
        # move normally and update the location
        mat[loc] = "X"
        loc = new_loc
    return mat

# returns true if traveling in given dir(direction) from loc(location)
# results in connecting on an existing path that travels in the same
# direction
def reaches_visited_path(mat,dirs,loc,dir):

    while True:
        if (dirs[loc] == dir.value):
            # pretty_print(mat)
            return True
        
        new_loc = tuple(move_once(loc,dir))
        if (not in_bounds(mat,new_loc)):
            mat[loc] = "="
            # exiting the matrix
            break
        
        if mat[new_loc] == "#":
            # hit a barrier
            break
        
        # move normally and update the location
        mat[loc] = "="
        loc = new_loc
    return False

# counts the number of possible obstacle locations to create a loop
# in the path of the guard
def count_loops(mat, loc, dir):
    
    count = 0
    # store the direction of the guard is facing when visiting each node
    dirs = np.full(mat.shape,-1)
    while True:
        new_loc = tuple(move_once(loc,dir))
        visited_marker = "X"
        
        if (not in_bounds(mat,new_loc)):
            # exiting the matrix
            mat[loc] = visited_marker
            dirs[loc] = dir.value
            break
        
        if mat[new_loc] == "#":
            # hit a barrier
            dir = rotate_right(dir)
            dirs[loc] = dir.value
            continue
        
        if (reaches_visited_path(np.copy(mat),dirs,loc,rotate_right(dir))):
            count += 1
            visited_marker = "+"
            # print(f"{count=}")
            # pretty_print(mat)
        
        
        # move normally and update the location
        mat[loc] = visited_marker
        dirs[loc] = dir.value
        loc = new_loc
    pretty_print(mat)
    return count


def problem_1():

    mat, start_location, start_direction = read_matrix()
    
    mat = mark_path(mat,start_location,start_direction)
    pretty_print(mat)

    # count of occurance of "X" in matrix
    sum = len(np.argwhere(mat=="X"))

    print(f'Part 1: {sum}')
    

def problem_2():
    
    mat, start_location, start_direction = read_matrix()
    
    count = count_loops(mat,start_location,start_direction)

    print(f'Part 2: {count}')

if __name__ == "__main__":
    problem_1()
    problem_2()