def min_max():
    list1 = [3, -1, 5, 5, 0]
    minimum = min(list1)
    maximum = max(list1)
    return tuple([minimum, maximum])

res = min_max()
print(res)



def unique_sorted():
    list2 = [1.0, 1, 2.5, 2.5, 0]
    sorted_set_list = sorted(set(list2))
    return sorted_set_list

ssl = unique_sorted()
print(ssl)



def flatten():
    list3 = [[1, 2], [3, 4]]
    list4 = []

    for sublist in list3:
        for item in sublist:
            if not isinstance(item, (int, float)):
                raise ValueError
            
    for sublist in list3:
        list4.extend(sublist)        
    return list4

list4 = flatten() 
print(list4)   