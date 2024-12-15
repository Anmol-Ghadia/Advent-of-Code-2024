from pathlib import Path 
import numpy as np

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
            row.append(int(char))
        matrix.append(row)
        
    return np.array(matrix)

# returns the four neighbors without bounds check
def get_neighbors(curr):
    assert len(curr) == 2
    out = []
    out.append([curr[0]-1   ,curr[1]])
    out.append([curr[0]     ,curr[1]+1])
    out.append([curr[0]+1   ,curr[1]])
    out.append([curr[0]     ,curr[1]-1])
    return out

def pretty_print(mat,mask):
    assert np.ndarray == type(mat)
    assert np.ndarray == type(mask)
    assert mat.shape == mask.shape
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            if mask[i,j] == True:
                print(mat[i, j],end='')
            else:
                print('.',end='')
        print()
    
# returns true if coord is present in the path
def coord_in_list(coord,path):
    assert len(coord) == 2
    for i in path:
        assert len(i) == 2
        if (coord[0] == i[0] and coord[1] == i[1]):
            return True
    return False

# returns the count of distinct end locations
def count_combined_paths(complete_paths):
    # print('='*10)
    end_locations = set()
    for i in complete_paths:
        # print(int(i[-1][0]), int(i[-1][1]))
        end_locations.add((int(i[-1][0]), int(i[-1][1])))
    # print(end_locations)
    # print(len(end_locations))
    return len(end_locations)

# Returns the count of trail ending locations (i.e. 9's)
# given a matrix, and start location (i.e. a 0)
def bfs(matrix, start_location):
    assert np.ndarray == type(matrix)
    assert len(start_location) == 2
    assert start_location[0] in range(matrix.shape[0])
    assert start_location[1] in range(matrix.shape[1])
    
    assert np.ndarray == type(matrix)
    to_visit = [[start_location]]
    complete_paths = []
    
    while len(to_visit) != 0:
        # mark current as visited
        curr_path = to_visit.pop(0)
        curr = curr_path[-1]
        
        if matrix[curr[0],curr[1]] == 9:
            complete_paths.append(curr_path)
            continue
        
        # iterate over all 4 neighbors
        for neighbor in get_neighbors(curr):
            
            # and not out of bounds
            if neighbor[0] not in range(matrix.shape[0]):
                continue
            if neighbor[1] not in range(matrix.shape[1]):
                continue
            
            # ignore the ones already visited
            if (coord_in_list(neighbor,curr_path)):
                continue
            
            # keep the neighbors that are +1 of current cell value
            if (matrix[neighbor[0],neighbor[1]] != matrix[curr[0],curr[1]]+1):
                continue
            
            # add valid neighbor to to_visit
            temp = curr_path[:]
            temp.append(neighbor)
            to_visit.append(temp)
    
    # pretty_print(matrix,visited)
    return len(complete_paths), count_combined_paths(complete_paths)

def problem_1():

    matrix = read_matrix()
    trailhead_locations = np.argwhere(matrix==0)
    end = 0
    for trailhead in trailhead_locations:
        _, endpoints = bfs(matrix,trailhead)
        end += endpoints
        
    print(f'Part 1: {end}')

def problem_2():

    matrix = read_matrix()
    trailhead_locations = np.argwhere(matrix==0)
    count = 0
    for trailhead in trailhead_locations:
        distinct, _ = bfs(matrix,trailhead)
        count += distinct
    
    print(f'Part 2: {count}')

if __name__ == "__main__":
    problem_1()
    problem_2()