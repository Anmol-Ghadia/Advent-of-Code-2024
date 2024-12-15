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
            row.append(char)
        matrix.append(row)
        
    return np.array(matrix)

def combination_no_dups(n):
    out = []
    for i in range(n):
        for j in range(i,n):
            if i != j:
                out.append([i,j])
    return out

def pretty_print(mat):
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            print(mat[i, j],end='')
        print()

def problem_1():

    matrix = read_matrix()
    
    # find all unique frequencies
    frequencies = np.unique(matrix)
    frequencies = frequencies[frequencies!='.']

    # find the indices of each type of frequency towers
    y_indices = range(matrix.shape[0])
    x_indices = range(matrix.shape[1])
    
    out = np.copy(matrix)
    out[np.ones(matrix.shape)==1] = '.'

    count = 0
    for freq in frequencies:
        curr_indices = np.argwhere(matrix==freq)
        if (len(curr_indices) == 1): 
            continue
        for index in combination_no_dups(len(curr_indices)):
            tower_1_index = curr_indices[index[0]]
            tower_2_index = curr_indices[index[1]]

            dy = abs(tower_1_index[0] - tower_2_index[0])
            dx = abs(tower_1_index[1] - tower_2_index[1])

            pos_1 = [None,None]
            pos_2 = [None,None]
            
            # assumes tower 1 is to right of tower 2
            pos_1[1] = tower_1_index[1]+dx
            pos_2[1] = tower_2_index[1]-dx
            if tower_1_index[1] < tower_2_index[1]:
                # tower 2 is to right of tower 1
                pos_1[1] = tower_1_index[1]-dx
                pos_2[1] = tower_2_index[1]+dx

            # assumes tower 1 is below tower 2
            pos_1[0] = tower_1_index[0]+dy
            pos_2[0] = tower_2_index[0]-dy
            if tower_1_index[0] < tower_2_index[0]:
                # tower 2 is to below of tower 1
                pos_1[0] = tower_1_index[0]-dy
                pos_2[0] = tower_2_index[0]+dy

            if (pos_1[0] in y_indices and pos_1[1] in x_indices and out[pos_1[0],pos_1[1]] == '.'):
                out[pos_1[0],pos_1[1]] = "#"
                count += 1
            if (pos_2[0] in y_indices and pos_2[1] in x_indices and out[pos_2[0],pos_2[1]] == '.'):
                out[pos_2[0],pos_2[1]] = "#"
                count += 1
    
    print(f'Part 1: {count}')
    
# TODO update to consider repeating antinodes with continued dy and dx's
def problem_2():
    
    matrix = read_matrix()
    
    # find all unique frequencies
    frequencies = np.unique(matrix)
    frequencies = frequencies[frequencies!='.']

    out = np.copy(matrix)
    out[np.ones(matrix.shape)==1] = '.'

    for freq in frequencies:
        curr_indices = np.argwhere(matrix==freq)
        if (len(curr_indices) == 1): 
            continue
        for index in combination_no_dups(len(curr_indices)):
            tower_1_index = curr_indices[index[0]]
            tower_2_index = curr_indices[index[1]]

            dy = tower_1_index[0] - tower_2_index[0]
            dx = tower_1_index[1] - tower_2_index[1]

            curr_y = tower_1_index[0]
            curr_x = tower_1_index[1]
            
            # search to one side
            while True:
                
                # check bounds
                if (curr_y not in range(out.shape[0])):
                    break
                if (curr_x not in range(out.shape[1])):
                    break
                
                # check overlap of antinode
                if (out[curr_y,curr_x] != "#"):
                    out[curr_y,curr_x] = "#"
                
                curr_y += dy
                curr_x += dx
                
            curr_y = tower_1_index[0]
            curr_x = tower_1_index[1]
            
            # search on the other side
            while True:
                
                # check bounds
                if (curr_y not in range(out.shape[0])):
                    break
                if (curr_x not in range(out.shape[1])):
                    break
                
                # check overlap of antinode
                if (out[curr_y,curr_x] != "#"):
                    out[curr_y,curr_x] = "#"
                
                curr_y -= dy
                curr_x -= dx
            
    print(f'Part 2: {len(np.argwhere(out=='#'))}')

if __name__ == "__main__":
    problem_1()
    problem_2()