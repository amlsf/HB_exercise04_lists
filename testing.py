def custom_pop(input_list):
    """custom_pop(input_list) imitates input_list.pop()"""
    last_item = input_list[-1]
    del input_list[-1]
    return last_item

def custom_insert(input_list, index, value):
    """custom_insert(input_list, index, value) imitates
    input_list.insert(index, value)
    """
    
    input_list[index:index] = [value]


def custom_append(input_list, value):
    """custom_append(input_list, value) imitates input_list.append(value)"""
#    input_list[:] += [value]

    input_list[len(input_list):] = [value]


"""
def custom_reverse(input_list):
    for i in range(len(input_list)):
        move = custom_pop(input_list)
        custom_insert(input_list,i,move)
# Why do I need a return here? 
    return input_list
"""

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


l = ['apple','bear','cat','dog','elephant']

print custom_reverse(l)


def custom_reverse(input_list):
    new_list = p[]