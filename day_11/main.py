from pathlib import Path 

def read_data():
    
    # read the input file
    with open(Path('given','input.txt'), 'r') as file:
        lines = file.readlines()
    
    line = lines[0].strip().strip('\n')
        
    # convert each number to int
    nums = {}
    for num in line.split(' '):
        num = int(num)
        if (num in nums.keys()):
            nums[num] += 1
        else:
            nums[num] = 1

    return nums

# returns the list of stone configuration after d levels
def recurse(nums, d):
    
    # termination condition
    if d == 0:
        return nums
    
    # compute stone configuration after one blink
    updated_nums = {}
    for stone in nums.keys():
        
        if (stone == 0):
            if (1 in updated_nums.keys()):
                updated_nums[1] += nums[stone]
            else:
                updated_nums[1] = nums[stone]
        elif (len(str(stone))%2 == 0):# even
            first = int(str(stone)[:len(str(stone))//2])
            second = int(str(stone)[len(str(stone))//2:])
            
            if (first in updated_nums.keys()):
                updated_nums[first] += nums[stone]
            else:
                updated_nums[first] = nums[stone]
            if (second in updated_nums.keys()):
                updated_nums[second] += nums[stone]
            else:
                updated_nums[second] = nums[stone]
        else:
            if (stone * 2024 in updated_nums.keys()):
                updated_nums[stone * 2024] += nums[stone]
            else:
                updated_nums[stone * 2024] = nums[stone]

    # print(updated_nums)
    del nums
    return recurse(updated_nums, d-1)

def problem_1():
    
    nums = read_data()
    final_stones = recurse(nums,25)
    
    # compute total
    total = 0
    for i in final_stones.keys():
        total += final_stones[i]

    print(f'Part 1: {total}')

def problem_2():
    nums = read_data()
    final_stones = recurse(nums,75)
    
    # compute total
    total = 0
    for i in final_stones.keys():
        total += final_stones[i]

    print(f'Part 2: {total}')
        
if __name__ == "__main__":
    problem_1()
    problem_2()