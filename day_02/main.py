from pathlib import Path

# returns 1 for ascending sort
#         0 for unsorted list
#         -1 for descending sort
def is_sorted(nums_arr):
    if nums_arr == sorted(nums_arr):
        return 1
    elif nums_arr == sorted(nums_arr, reverse=True):
        return -1
    return 0

# returns true if each element in arr is increasing by 1,2 or 3
def has_valid_increasing_difference(arr):
    old_num = arr[0]
    for new_num in arr[1:]:
        diff = new_num - old_num
        if (diff not in list(range(1,4))):
            return False
        old_num = new_num
    return True

# returns true if each element in arr is decreasing by 1,2 or 3
def has_valid_decreasing_difference(arr):
    old_num = arr[0]
    for new_num in arr[1:]:
        diff = old_num - new_num
        if (diff not in list(range(1,4))):
            return False
        old_num = new_num
    return True

# returns true if adjacent elements differ by 1,2 or 3
#            and is sorted (either acending or descending)
def is_valid_report(arr):
    sort_dir = is_sorted(arr)
    if (sort_dir == 1 and has_valid_increasing_difference(arr)):
        return True
    elif (sort_dir == -1 and has_valid_decreasing_difference(arr)):
        return True
    else:
        return False

def problem_1():
    # read the input file
    with open(Path('given','input.txt'), 'r') as file:
        lines = file.readlines()
    
    # remove newline character
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n','')
        
    # convert each line into numbers
    nums = []
    for i in range(len(lines)):
        lineArr = lines[i].split(' ')
        singleReportArr = []
        for num in lineArr:
            singleReportArr.append(int(num))
        nums.append(singleReportArr)
    
    # keep reports that are sorted and have valid level difference
    valid_reports = []
    for arr in nums:
        if (is_valid_report(arr)):
            valid_reports.append(arr)
    
    print(f'Part 1: {len(valid_reports)}')

# given a list, returns multiple copies of the list with 
# one element missing in each
def produce_mutant_lists(initial_arr):
    out_arr = []
    for i in range(len(initial_arr)):
        tempArr = initial_arr[:]
        tempArr.pop(i)
        out_arr.append(tempArr)
    return out_arr

def problem_2():
    # read the input file
    with open(Path('given','input.txt'), 'r') as file:
        lines = file.readlines()
    
    # remove newline character
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n','')
        
    # convert each line into numbers
    nums = []
    for i in range(len(lines)):
        lineArr = lines[i].split(' ')
        singleReportArr = []
        for num in lineArr:
            singleReportArr.append(int(num))
        nums.append(singleReportArr)
    
    # keep reports that are sorted and have valid level difference
    valid_reports = []
    for initial_arr in nums:
        for modified_arr in produce_mutant_lists(initial_arr):
            if (is_valid_report(modified_arr)):
                valid_reports.append(modified_arr)
                break
    
    print(f'Part 2: {len(valid_reports)}')
    
if __name__ == "__main__":
    problem_1()
    problem_2()