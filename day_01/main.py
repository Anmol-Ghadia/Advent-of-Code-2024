from pathlib import Path 

def problem_1():
    # read the input file
    with open(Path('given','input.txt'), 'r') as file:
        lines = file.readlines()
    
    # remove newline character
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n','')
        
    # convert each line into numbers
    nums_0 = []
    nums_1 = []
    for i in range(len(lines)):
        tempArr = lines[i].split(' ')
        nums_0.append(int(tempArr[0]))
        nums_1.append(int(tempArr[-1]))
    
    # sort the arrays
    nums_0.sort()
    nums_1.sort()
    
    # compute sum of absolute difference
    sum = 0
    for i in range(len(nums_1)):
        sum += abs(nums_0[i]-nums_1[i])
    
    print(f'Part 1: {sum}')
    

def problem_2():
    # read the input file
    with open(Path('given','input.txt'), 'r') as file:
        lines = file.readlines()
    
    # remove newline character
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n','')
        
    # convert each line into numbers
    nums_0 = []
    nums_1 = []
    for i in range(len(lines)):
        tempArr = lines[i].split(' ')
        nums_0.append(int(tempArr[0]))
        nums_1.append(int(tempArr[-1]))
    
    # count occurance of each element of nums_0 in nums_1
    similarity = 0
    for num in nums_0:
        similarity += num * nums_1.count(num)
        
    print(f'Part 2: {similarity}')
        
if __name__ == "__main__":
    problem_1()
    problem_2()