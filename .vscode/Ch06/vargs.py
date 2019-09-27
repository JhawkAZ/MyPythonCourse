some_nums=[2,6,9,23,48,15,25,16]
def slice_list(list_to_slice, *upper_bounds):
    """ Returns one list of results for all bounds passed in"""
    list_to_return=[]
    for upper_bound in upper_bounds:
        if (len(list_to_slice)>upper_bound):
            print('Slicing...')
            list_to_return.append(list_to_slice[:upper_bound])
        else:
            list_to_return.append(None)
        
    return list_to_return

print(slice_list(some_nums,2))
