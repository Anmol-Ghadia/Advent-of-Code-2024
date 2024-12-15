from pathlib import Path 

class DiskUnit:
    def __init__(self, id, length, free=False):
        self.id = id
        self.__is_free = free
        self.length = length

    def is_free(self):
        return self.__is_free

    def is_file(self):
        return not self.__is_free
    
    def get_id(self):
        return self.id
    
    def to_free(self):
        self.__is_free = True
        self.id = None

    def to_file(self, id):
        if not self.__is_free:
            raise ValueError("ALREADY a file unit")
        self.__is_free = False
        self.id = id
    
    def set_length(self, new_length):
        self.length = new_length

    def __len__(self):
        return self.length

    def __str__(self):
        return f"DiskUnit(id={self.id}, length={self.length}, is_free={self.__is_free})"


def read():
    # read the input file
    with open(Path('given','input.txt'), 'r') as file:
        lines = file.readlines()
    
    line = lines[0].strip().strip('\n')
    
    out = []
    id = 0
    for i in range(len(line)):
        curr = int(line[i])
        
        # create file/free unit
        if i%2 == 0: # is file
            du = DiskUnit(id, curr)
            id += 1
        else:
            du = DiskUnit(None, curr,True)
        
        out.append(du)
    
    return out

def pretty_print(disk_units):
    for du in disk_units:
        if du.is_file():
            print(f'{du.get_id()}'*len(du),end='')
        else:
            print(f'.'*len(du),end='')
    print()
    

# returns true if all free disk units are on the right
def all_free_space_on_right(disk_units):
    seen_free = False
    for du in disk_units:
        if du.is_file():
            if seen_free:
                return False
        else:
            seen_free = True
    return True

# returns the first file from right
def get_first_file_from_right(disk_units):
    for i in range(len(disk_units)-1,0,-1):
        du = disk_units[i]
        if (du.is_file()):
            return du, i
    
    raise "No file found"

# returns the first free unit from left
def get_first_free_from_left(disk_units,length=None):
    for i in range(len(disk_units)):
        du = disk_units[i]
        if (du.is_free()):
            if length == None:
                return du, i
            if length <= len(du):
                return du, i
    
    raise "No free unit found"

# returns the modified disk units    
def move_files_left(disk_units):
    while (not all_free_space_on_right(disk_units)):
        
        # find the first file from right
        right_file, file_idx = get_first_file_from_right(disk_units)
        
        # insert as much as possible to the leftmost free space
        left_free, free_idx = get_first_free_from_left(disk_units)
        
        if (len(right_file) == len(left_free)):
            # remove left_free, and replace it with right_file
            left_free.to_file(right_file.get_id())
            right_file.to_free()
        
        elif (len(right_file) < len(left_free)):
            # remove right_file, and add before left free, modify lengths
            right_file_copy = DiskUnit(right_file.get_id(),len(right_file))
            disk_units.insert(free_idx,right_file_copy)
            right_file.to_free()
            left_free.set_length(len(left_free) - len(right_file))
        
        else:
            # replace the left_free with as much of right file as possible
            # keep right file with reduced length, left_free is removed
            right_file.set_length(len(right_file) - len(left_free))
            
            left_free_copy = DiskUnit(None,len(left_free),True)
            disk_units.insert(file_idx,left_free_copy)
            
            left_free.to_file(right_file.get_id())

# returns the maximum id
def find_max_id(disk_units):
    curr_max_id = 0
    for du in disk_units:
        if (not du.is_file()):
            continue
        if (du.get_id() > curr_max_id):
            curr_max_id = du.get_id()
    return curr_max_id

def get_unit_by_id(disk_units, id):
    for i in range(len(disk_units)):
        du = disk_units[i]
        if (du.get_id() != None and du.get_id() == id):
            return du, i
    
    raise "no disk unit with given id not found"

# returns the modified disk units
def move_files_left_without_fragmentation(disk_units):
    curr_id = find_max_id(disk_units) + 1
    while True:
        if (curr_id == 0):
            break
        
        curr_id -= 1
        
        right_file, file_idx = get_unit_by_id(disk_units,curr_id)
        
        try:
            left_free, free_idx = get_first_free_from_left(disk_units,len(right_file))
            
            if (free_idx > file_idx): 
                continue
            
            if (len(right_file) == len(left_free)):
                # remove left_free, and replace it with right_file
                left_free.to_file(right_file.get_id())
                right_file.to_free()
            
            else:
                # remove right_file, and add before left free, modify lengths
                right_file_copy = DiskUnit(right_file.get_id(),len(right_file))
                disk_units.insert(free_idx,right_file_copy)
                right_file.to_free()
                left_free.set_length(len(left_free) - len(right_file))
                
        except Exception:
            pass

def checksum(disk_units):
    total = 0
    idx = 0
    for du in disk_units:
        for i in range(len(du)):
            if (du.is_file()):
                total += du.get_id() * idx
            idx += 1
    return total

def problem_1():
    disk_units = read()
    move_files_left(disk_units)
    print(f'Part 1: {checksum(disk_units)}')
    
def problem_2():
    disk_units = read()
    move_files_left_without_fragmentation(disk_units)
    print(f'Part 2: {checksum(disk_units)}')

if __name__ == "__main__":
    problem_1()
    problem_2()