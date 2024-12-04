from pathlib import Path 
import re

def problem_1():
    # read the input file
    with open(Path('given','input.txt'), 'r') as file:
        rawInput = file.read()
    
    # remove newline character
    rawInput = rawInput.replace('\n','')
        
    # find all valid instances of substring
    result = re.findall(r'mul\(\d{1,3},\d{1,3}\)', rawInput)
    
    # compute the sum of multiplications
    sum = 0
    for item in result:
        nums = re.findall(r'\d{1,3}', item)
        assert len(nums) == 2
        sum += int(nums[0]) * int(nums[1])
        
    print(f'Part 1: {sum}')
    

def problem_2():
    # read the input file
    with open(Path('given','input.txt'), 'r') as file:
        rawInput = file.read()
    
    # remove newline character
    rawInput = rawInput.replace('\n','')
        
    # find all valid instances of substring
    result = re.findall(r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))", rawInput)
    
    # compute the sum of multiplications
    sum = 0
    do_multiply = True
    for item in result:
        # found mul
        if (re.match(r'mul\(\d{1,3},\d{1,3}\)', item)):    
            # skip if encountered "don't()" recently
            if (not do_multiply):
                continue
            
            nums = re.findall(r'\d{1,3}', item)
            assert len(nums) == 2
            sum += int(nums[0]) * int(nums[1])
        
        # flip to do()
        elif (re.match(r'do\(\)', item)):
            do_multiply = True
        
        # flip to don't()
        elif (re.match(r"don't\(\)",item)):
            do_multiply = False
        
        # failure case
        else:
            raise "Unexpected Error"

    print(f'Part 2: {sum}')
        
if __name__ == "__main__":
    problem_1()
    problem_2()