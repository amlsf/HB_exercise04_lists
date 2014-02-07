def custom_contains(input_list, value):
    """custom_contains(input_list, value) imitates (value in input_list)"""
    i = 0

    while False:
        if input_list[i] == value:
            print "Testing list item: %r in index #: " % (input_list[i], i)
            print True
            break
        else: 
            print "Testing list item: %r in index #: " % (input_list[i], i)
            print False
            i += 1

input_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
                       'Sep', 'Oct', 'Nov', 'Dec']


print custom_contains(input_list, 'Jan')