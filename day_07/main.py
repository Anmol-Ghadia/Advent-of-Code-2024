from pathlib import Path

def read_data():
    
    # read the input file
    with open(Path('given','input.txt'), 'r') as file:
        lines = file.readlines()
    
    # remove newline character
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n','')
        
    # convert each line into numbers
    nums = []
    for i in range(len(lines)):
        test_nums = lines[i].split(':')
        temp = []
        for num in test_nums[1].split(" "):
            if (num == ''):
                continue
            temp.append(int(num))
        nums.append([int(test_nums[0]),temp])

    return nums

def problem_1():
    
    # returns true if there exists a way to combine the elements of arr
    # using just the multiplication and addition operators to get val
    def recursive_check(val, arr):
        if (len(arr) == 0):
            return True

        # base case
        if (len(arr) == 1):
            return val == arr[0]

        if recursive_check(val - arr[-1], arr[:-1]):
            return True
        if recursive_check(val / arr[-1], arr[:-1]):
            return True
        
        return False

    # start of problem_1
    nums = read_data()

    # sum the test value for valid liens
    sum = 0
    for pair in nums:
        assert len(pair) == 2
        if (recursive_check(pair[0], pair[1])):
            sum += pair[0]
        
    print(f'Part 1: {sum}')

def problem_2():
    
    # returns array of all possible values given the operands and 
    # multiplication, addition and concatenation operators
    def recursive_check(val, arr):
        if len(arr) == 0:
            return False
        if len(arr) == 1:
            return arr[0] == val
        
        first_ele = arr[0]
        second_ele = arr[1]
        sum_arr = [first_ele + second_ele] + arr[2:]
        prod_arr = [first_ele * second_ele] + arr[2:]
        concat_arr = [int(f"{first_ele}{second_ele}")] + arr[2:]

        return recursive_check(val,sum_arr) or recursive_check(val, prod_arr) or recursive_check(val, concat_arr)

    # start of problem_2
    nums = read_data()

    # sum the test value for valid liens
    sum = 0
    for pair in nums:
        assert len(pair) == 2
        if (recursive_check(pair[0], pair[1])):
            sum += pair[0]

    print(f'Part 2: {sum}')
    
if __name__ == "__main__":
    problem_1()
    problem_2()