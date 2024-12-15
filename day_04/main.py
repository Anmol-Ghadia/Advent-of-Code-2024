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

def problem_1():

    # returns string corresponding to coordinates
    #           returns None if out of bounds
    def get_elements_from_coords(mat,indices):
        out = []
        for coord in indices:
            if (coord[0] < 0 or coord[1] < 0):
                return None
            try:
                out.append(mat[coord[0],coord[1]])
            except:
                return None
        return ''.join(out)

    # finds the word XMAS in up direction
    def has_word_up(mat,x,y):
        coords = []
        for i in range(len(WORD)):
            coords.append([y-i,x])
            
        return WORD == get_elements_from_coords(mat,coords)

    # finds the word XMAS in up and right directions
    def has_word_up_right(mat,x,y):
        coords = []
        for i in range(len(WORD)):
            coords.append([y-i,x+i])
            
        return WORD == get_elements_from_coords(mat,coords)

    # finds the word XMAS in right direction
    def has_word_right(mat,x,y):
        coords = []
        for i in range(len(WORD)):
            coords.append([y,x+i])
            
        return WORD == get_elements_from_coords(mat,coords)

    # finds the word XMAS in down and right direction
    def has_word_down_right(mat,x,y):
        coords = []
        for i in range(len(WORD)):
            coords.append([y+i,x+i])
            
        return WORD == get_elements_from_coords(mat,coords)

    # finds the word XMAS in down direction
    def has_word_down(mat,x,y):
        coords = []
        for i in range(len(WORD)):
            coords.append([y+i,x])
            
        return WORD == get_elements_from_coords(mat,coords)

    # finds the word XMAS in down and left direction
    def has_word_down_left(mat,x,y):
        coords = []
        for i in range(len(WORD)):
            coords.append([y+i,x-i])
            
        return WORD == get_elements_from_coords(mat,coords)

    # finds the word XMAS in left direction
    def has_word_left(mat,x,y):
        coords = []
        for i in range(len(WORD)):
            coords.append([y,x-i])
            
        return WORD == get_elements_from_coords(mat,coords)


    # finds the word XMAS in up and left direction
    def has_word_up_left(mat,x,y):
        coords = []
        for i in range(len(WORD)):
            coords.append([y-i,x-i])
            
        return WORD == get_elements_from_coords(mat,coords)

    # returns the count of WORD that starts from given coords
    def find_num_matches(mat,x,y):
        directions = [
            has_word_up,
            has_word_up_right,
            has_word_right,
            has_word_down_right,
            has_word_down,
            has_word_down_left,
            has_word_left,
            has_word_up_left
        ]
        
        count = 0
        for direction in directions:
            if direction(mat, x, y):
                count += 1
        return count
    
    # Start of problem_1
    WORD = "XMAS"
    mat = read_matrix()
    
    # compute matches by summing match at each coordinate
    total_matches = 0
    for y in range(mat.shape[0]):
        for x in range(mat.shape[1]):
            total_matches += find_num_matches(mat,x,y)

    print(f'Part 1: {total_matches}')
    

def problem_2():

    # returns string corresponding to coordinates
    #           returns None if out of bounds
    def get_elements_from_coords(mat,indices):
        out = []
        for coord in indices:
            if (coord[0] < 0 or coord[1] < 0):
                return None
            try:
                out.append(mat[coord[0],coord[1]])
            except:
                return None
        return ''.join(out)

    # finds the WORD in forward slash centered at x,y
    def has_word_forward_slash(mat,x,y):
        coords = []
        coords.append([x-1,y+1])
        coords.append([x,y])
        coords.append([x+1,y-1])
            
        extracted = get_elements_from_coords(mat,coords)
        if (extracted == None): return False
        if (WORD == extracted): return True
        if (WORD[::-1] == extracted): return True
        return False

    # finds the WORD in backward slash centered at x,y
    def has_word_backward_slash(mat,x,y):
        coords = []
        coords.append([x+1,y+1])
        coords.append([x,y])
        coords.append([x-1,y-1])
        
        extracted = get_elements_from_coords(mat,coords)
        if (extracted == None): return False
        if (WORD == extracted): return True
        if (WORD[::-1] == extracted): return True
        return False

    # returns the count of WORD that starts from given coords
    def has_match(mat,x,y):
        return has_word_forward_slash(mat, x, y) and has_word_backward_slash(mat,x,y)
    
    # Start of problem_2
    WORD = "MAS"
    mat = read_matrix()
    
    # compute matches by summing match at each coordinate
    total_matches = 0
    for y in range(mat.shape[0]):
        for x in range(mat.shape[1]):
            if has_match(mat,x,y):
                total_matches += 1 
        
    print(f'Part 2: {total_matches}')

if __name__ == "__main__":
    problem_1()
    problem_2()