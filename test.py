input_list = [0,1,2,3]

def custom_append(input_list, value):
    """custom_append(input_list, value) imitates input_list.append(value)"""
#    input_list[:] += [value]

    input_list[len(input_list):] = [value]


def custom_pop(input_list):
    """custom_pop(input_list) imitates input_list.pop()"""
    last_item = input_list[-1]
    del input_list[-1]
    return last_item


def custom_reverse(input_list):
    """ custom_reverse(input_list) imitates input_list.reverse()"""
    new_list = []

    for i in range(len(input_list)):
        new_item = custom_pop(input_list[i])
        custom_append(new_list, new_item)

print custom_pop(input_list)

print input_list

custom_append(input_list, "5")

print input_list

custom_reverse(input_list)

print input_list

# print custom_reverse(input_list)