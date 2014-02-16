
"""
Part 1: Fundamental operations on lists
---------------------------------------

The fundamental operations on lists in Python are those that are part of the
language syntax and/or cannot be implemented in terms of other list operations:
    * List literals ([], ['hello'], [3, 1, 4, 1, 5, 9], etc.)
    * List indexing (some_list[index])
    * List indexing assignment (some_list[index] = value)
    * List slicing (some_list[start:end])
    * List slicing assignment (some_list[start:end] = another_list)
    * List index deletion (del some_list[index])
    * List slicing deletion (del some_list[start:end])

In this section you will implement functions that each use just one of the
operations. The docstring of each function describes what it should do. Consult
test_list_operations.py for concrete examples of the expected function behavior.
"""

def head(input_list):
    """Return the first element of the input list."""
    return input_list[0]

def tail(input_list):
    """Return all elements of the input list except the first."""
    return input_list[1:]

def last(input_list):
    """Return the last element of the input list."""
    return input_list[-1]

def init(input_list):
    """Return all elements of the input list except the last."""
    return input_list[:-1]

def first_three(input_list):
    """Return the first three elements of the input list."""
    return input_list[:3]

def last_five(input_list):
    """Return the last five elements of the input list."""
    return input_list[-5:]

def middle(input_list):
    """Return all elements of the input list except the first two and the last
    two.
    """
    return input_list[2:-2]

def inner_four(input_list):
    """Return the third, fourth, fifth, and sixth elements of the input list."""
    return input_list[2:6]

def inner_four_end(input_list):
    """Return the sixth, fifth, fourth, and third elements from the end of the
    list, in that order.
    """
    return input_list[-6:-2]

def replace_head(input_list):
    """Replace the head of the input list with the value 42."""
    input_list[0] = 42

def replace_third_and_last(input_list):
    """Replace the third and last elements of the input list with the value 37."""
    input_list[2] = 37
    input_list[-1] = 37

def replace_middle(input_list):
    """Replace all elements of the input list with the the values 42 and 37, in
    that order, except for the first two and last two elements.
    """

    input_list[2:-2] = [42, 37]

"""
    for i in range(2,len(input_list)-2,2):
        input_list[i] = 42

    for i in range(3,len(input_list)-2,2):
        input_list[i] = 37
"""

def delete_third_and_seventh(input_list):
    """Remove the third and seventh elements of the input list."""
    del input_list[6]
    del input_list[2]

def delete_middle(input_list):
    """Remove all elements from the input list except for the first two and the
    last two.
    """
    del input_list[2:-2]

"""
Part 2: Derived operations on lists
-----------------------------------

In this section you will implement your own versions of the standard list methods.
You should use only the primitive operations from Part 1 in your implementations.
For loops are also allowed, such as the following:
    for element in some_list:
        # Do something with element

Each custom method imitates a built-in list method, as described by the docstring
for each function. Play with the built-in methods in the Python REPL to get a feel
for how they work before trying to write your custom version. You may also look at
the test_list_operations.py file for concrete examples of expected behavior.
"""

def custom_len(input_list):
    """custom_len(input_list) imitates len(input_list)"""
    x = 0

    for i in input_list:
        x += 1

    return x

# For the next four functions, get clever using slice operations described in the first half
def custom_append(input_list, value):
    """custom_append(input_list, value) imitates input_list.append(value)"""
#    input_list[:] += [value]

    input_list[len(input_list):] = [value]

def custom_extend(input_list, values):
    """custom_extend(input_list, values) imitates input_list.extend(values)"""
    for i in range(len(values)): 
        #input_list[:] += [values[i]]
        input_list[len(input_list):] = [values[i]]

    return input_list

def custom_insert(input_list, index, value):
    """custom_insert(input_list, index, value) imitates
    input_list.insert(index, value)
    """
    
    input_list[index:index] = [value]

def custom_remove(input_list, value):
    """custom_remove(input_list, value) imitates input_list.remove(value)"""
    
    for i in range(len(input_list)):
        if input_list[i] == value:
            del input_list[i]
            break

def custom_pop(input_list):
    """custom_pop(input_list) imitates input_list.pop()"""
    last_item = input_list[-1]
    del input_list[-1]
    return last_item

def custom_index(input_list, value):
    """custom_index(input_list, value) imitates input_list.index(value)"""
    for i in range(len(input_list)):
        if input_list[i] == value:
            return i
            break

def custom_count(input_list, value):
    """custom_count(input_list, value) imitates input_list.count(value)"""
    counter = 0

    for i in range(len(input_list)):
        if input_list[i] == value:
            counter +=1
    
    return counter
    

# TODO - try this with the input_list = [::-1] (Does that return the list same place in memory or a copy?)
# why does this function require the original list to be changed in memory, while others can accept copies? (oh right, it was because of the testing python program somehow)
# Because the test_list_operations used "self" to reference itself in memory

# Need to fix this and understand why this doesn't work in memory???
# TODO  Why doesn't this worK: input_list = input_list[::-1]? What's a better way to do this??
#           Because it creates a copy? 


def custom_reverse(input_list):
    """ custom_reverse(input_list) imitates input_list.reverse()"""
    for i in range(len(input_list)):
        move = custom_pop(input_list)
        custom_insert(input_list,i,move)
# Why do I need a return here? 
    return input_list

"""
TODO - look at this
ANOTHER METHOD
def custom_reverse(input_list):
    """custom_reverse(input_list) imitates input_list.reverse()"""
    half_length = custom_len(input_list) // 2
    for i in range(half_length):
        # Swap the corresponding pair of values in place.
        input_list[i], input_list[-i-1] = input_list[-i-1], input_list[i]
"""


"""    
SUCCESSFUL METHOD 2
    tmp = 0
    counter_bkwd = len(input_list)-1

    for i in range(len(input_list)/2):

        tmp = input_list[i]

        input_list[i] = input_list[counter_bkwd]
        input_list[counter_bkwd] = tmp

        i += 1        
        counter_bkwd = counter_bkwd - 1
"""

"""
SUCCESFUL METHOD 2 WITH PRINT STATEMENTS
Successful Method 2   
    tmp = 0
    counter_bkwd = len(input_list)-1

    for i in range(len(input_list)/2):
        print "START OF LOOP: this is the backwards counter: %r" % counter_bkwd
        print "This is the list before modification: %r" % input_list

        tmp = input_list[i]
        print "this is the stored first variable to move to the end: %r" % tmp

        input_list[i] = input_list[counter_bkwd]
        print "This is the modified list with the last moved to front: %r" % input_list

        input_list[counter_bkwd] = tmp
        print "This is the modified list with the front moved to the back: %r" % input_list

        i += 1
        print "This is the forwards counter: %r" % i
        
        counter_bkwd = counter_bkwd - 1
        print "This is the backwards counter: %r" % counter_bkwd
"""

"""
Failed Method

def custom_reverse(input_list):
    new_list = []
    for i in range(len(input_list)-1,-1,-1):
        print "The range is:"
        print range(len(input_list)-1,-1,-1)
        print "The last term to pop is: ", input_list[i]
        new_item = custom_pop(input_list)
        print "The new item is:", new_item
        print "This is the new appended list:"
        custom_append(new_list, new_item)
        print new_list
"""



def custom_contains(input_list, value):
    """custom_contains(input_list, value) imitates (value in input_list)"""
    for item in input_list:
        if item == value:
            return True
# Need to put return False statement outside of For Loop, if True will break with return True
    return False

"""
SUCCESSFUL METHOD 2

    for i in range(len(input_list)):
        if input_list[i] == value:
            return True
    return False
"""

"""
SUCCESSFUL METHOD 3
    i = 0
        ## VVV Expression goes here
    while i < len(input_list):
        if input_list[i] == value:
            return True
            break
        i += 1
    return False

"""


def custom_equality(some_list, another_list):
    """custom_equality(some_list, another_list) imitates
    (some_list == another_list)
    """
    if some_list == another_list: 
        return True
    else: 
        return False


"""
SUCCESSFUL (but super verbose) METHOD
    counter = 0

    if len(some_list) == len(another_list):
        for i in range(len(some_list)):
            if some_list[i] == another_list[i]:
                counter += 1
            else: 
                counter += 0
    else: 
        return False

    if counter == len(some_list):
        return True
    else: 
        return False
"""