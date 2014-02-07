input_list = [0,"hello",2,3]
second_list = [0,"hello",2,3]
other_list = ["aweseom",1,2,5]

def custom_append(input_list, value):
    """custom_append(input_list, value) imitates input_list.append(value)"""
#    input_list[:] += [value]

    input_list[len(input_list):] = [value]


def custom_pop(input_list):
    """custom_pop(input_list) imitates input_list.pop()"""
    last_item = input_list[-1]
    del input_list[-1]
    return last_item

#======================================================================================================================

##### PROBLEM #1

def custom_reverse(input_list):
    """ custom_reverse(input_list) imitates input_list.reverse()"""
    new_list = []
    for i in range(len(input_list)-1,-1,-1):
custom_append(new_list, input_list[i])
#    input_list = new_list
    return new_list

# This works with print but not with return... why??????

print custom_pop(input_list)

print input_list

custom_append(input_list, "5")

print input_list


# This works but doesn't actually change the input_list, just shows if call with the function...why????:
# "print input_list" doesn't work, but print function does
print custom_reverse(input_list)




##### PROBLEM #2

# This works except when it is False, it returns None. How do I get it to return a True? 
# Close just need to add a return False at the end outside of the for loop
def custom_contains(input_list, value):
    """custom_contains(input_list, value) imitates (value in input_list)"""
    for i in range(len(input_list)):
        if input_list[i] == value:
            return True


print custom_contains(input_list, 5)




##### PROBLEM #3

# Doesn't work, only returns false
def custom_equality(some_list, another_list):
    """custom_equality(some_list, another_list) imitates
    (some_list == another_list)
    """
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


print custom_equality(input_list, second_list)