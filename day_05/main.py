from pathlib import Path 
import numpy as np

def read_data():
    # read the input file
    with open(Path('given','input.txt'), 'r') as file:
        lines = file.readlines()
    
    # remove newline character
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n','')
    
    # remove newline character
    found_sep = False
    rules = []
    orderings = []
    for i in range(len(lines)):
        if lines[i] == '':
            found_sep = True
            continue
        if not found_sep:
            rules.append(lines[i].split('|'))
        else:
            orderings.append(lines[i].split(','))
            
    rules_out = []
    for i in rules:
        temp = []
        for j in i:
            temp.append(int(j))
        rules_out.append(tuple(temp))
    
    orderings_out = []
    for i in orderings:
        temp = []
        for j in i:
            temp.append(int(j))
        orderings_out.append(temp)
    
    return tuple(rules_out), orderings_out

# returns the index of item in right list that violates the rule
# else returns -1
def find_invalid_index(rules, element, right):

    # returns true if to_check exists in list of rules
    def contains_ordering(to_check):
        for rule in rules:
            if (rule[0] == to_check[0] and rule[1] == to_check[1]):
                return True
        return False


    for i in range(len(right)):
        item = right[i]
        if not contains_ordering([element,item]):
            return i
    return -1

# returns true if the ordering is correct according to rules
def is_correct(rules, order):
    for i in range(len(order)):
        right = []
        if (i+1 < len(order)):
            right = order[i+1:]
        
        incorrect_index = find_invalid_index(rules,order[i],right)
        if (incorrect_index != -1):
            return False
        
    return True

def problem_1():
    rules, orderings = read_data()
    
    # filter and collect correct orderings
    correct_orderings = []
    for order in orderings:
        valid = is_correct(rules, order)
        if valid:
            correct_orderings.append(order)
    
    sum = 0
    for ordering in correct_orderings:
        sum += ordering[len(ordering)//2]

    print(f'Part 1: {sum}')

def problem_2():
    rules, orderings = read_data()
    
    # filter and collect incorrect orderings
    incorrect_orderings = []
    for order in orderings:
        valid = is_correct(rules, order)
        if not valid:
            incorrect_orderings.append(order)
    
    # given an ordering and rules,
    # returns the fixed ordering
    def fix_ordering(ordering):
        temp_ordering = ordering[:]
        loop = True
        while loop:
            for i in range(len(temp_ordering)):
                
                # check if order is correct
                right = []
                if (i+1 < len(temp_ordering)):
                    right = temp_ordering[i+1:]
                
                incorrect_index = find_invalid_index(rules, temp_ordering[i],right)
                if (incorrect_index != -1):
                    # otherwise flip order and loop
                    temp = temp_ordering[i+incorrect_index+1]
                    temp_ordering[i+incorrect_index+1] = temp_ordering[i]
                    temp_ordering[i] = temp
                    break
                
                if (i == len(temp_ordering)-1):
                    loop = False
            
        return temp_ordering
    
    # fix orderings
    fixed_orderings = []
    for ordering in incorrect_orderings:
        fixed_orderings.append(fix_ordering(ordering))
    
    # compute the sum of middle elements
    sum = 0
    for ordering in fixed_orderings:
        sum += ordering[len(ordering)//2]

    print(f'Part 2: {sum}')

if __name__ == "__main__":
    problem_1()
    problem_2()