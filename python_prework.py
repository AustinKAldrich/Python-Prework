#Question 1:
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
#The first line of the code has been defined as below.

def hello_name(user_name):
    """Print "hello_USERNAME!" """
    print("hello_" + user_name.upper() + "!")


#Question 2:
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    """Print all the odd numbers between 1 and 100"""
    for num in range(1,100,2):
        print(num)

#Question 3:
#Please write a Python function, max_num_in_list to return the max number of a given list.
# The first line of the code has been defined as below.

def max_num_in_list(a_list):
    """Return the largest number in a given list."""
    sorted_list = sorted(a_list[:])
    return sorted_list[-1]

#The above function was my first idea, but then I found this already integrated "max" function, so I streamlined below.
def maximum(lst):
    """Return the largest number in a given list."""
    return max(lst)

#Question 4:
#Write a function to return if the given year is a leap year. 
#A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
#The return should be boolean Type (true/false).

def is_leap_year(a_year):
    """Return whether or not a given year is a leap year."""
    if a_year % 4 == 0 and a_year % 400 == 0:
        return True
    elif a_year % 4 == 0 and a_year % 100 == 0:
        return False
    elif a_year % 4 == 0:
        return True
    else:
        return False
    
#Question 5:
#Write a function to check to see if all numbers in list are consecutive numbers. 
#For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
#The return should be boolean Type.
    
def simple_consecutive(smaller_num, larger_num):
    """Determines whether two numbers are consecutive"""
    if smaller_num == larger_num - 1:
        return True
    else:
        return False
    
def is_consecutive(a_list):
    """Determines whether all of the numbers in a given list are consecutive."""
    index = 0
    next_index = 1
    length = len(a_list)
    while next_index < length:
        if simple_consecutive(a_list[index], a_list[next_index]) == False:
            return False
            break
        elif simple_consecutive(a_list[index], a_list[next_index]) == True:
            index += 1
            next_index += 1
            if next_index < length:
                continue
            else:
                return True


    
test_list = [6,7,8,91,10,11]

print(is_consecutive(test_list))
