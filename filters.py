def get_max_temp(my_dict):
    #method 1
    cities = []
    for title, city in my_dict.items():
        highs = []
        for month, vals in city['Climate'].items():
            highs.append(vals['Record high'])
        cities.append((title, max(highs)))
    print('\n')
    print(cities)

    cities_2 = _filter_dict_by_path(my_dict, ['Climate', 'Record high'])
    print('\n')
    print(cities_2)

    cities_3 = _filter_dict_by_path_and_func(my_dict, ['Record high'], lambda v: float(v) >= 19)
    print('\n')
    print(cities_3)

    for city, vals in cities_2.items():
        fields = _get_matching_fields(vals, 'Record high')
        print(f'{city}: max temp == {max(fields)}')

    print('\n')
    for city, vals in _filter_dict_by_path(my_dict, ['Mar']).items():
        fields = _get_matching_fields(vals, 'Record high')
        print(f'{city}: max temp == {max(fields)}')
    
    return cities

'''
I want to break up the problem of filtering.
1. Apply multiple filters easily
2. Make filters in a DRY fashion
'''
def _filter_dict_by_path(my_dict, path):
    # this checks if all of path appears, but not if it appears without gaps
    if len(path) == 0:
        return {}
    new_dict = {}
    for k, v in my_dict.items():
        if k == path[0] and len(path) == 1:
            new_dict[k] = v
        elif isinstance(v, dict):
            if k == path[0]:
                val = _filter_dict_by_path(v, path[1:])
            else:
                val = _filter_dict_by_path(v, path)
            if val:
                new_dict[k] = val
    return new_dict


def _filter_dict_by_path_and_func(my_dict, path, func):
    # this checks if all of path appears, but not if it appears without gaps
    # the last path item must be the key of the value to be checked
    # func is a function that returns a bool
    if len(path) == 0:
        return {}
    new_dict = {}
    for k, v in my_dict.items():
        if k == path[0] and len(path) == 1 and not isinstance(v, dict) and func(v):
            new_dict[k] = v
        elif isinstance(v, dict):
            if k == path[0]:
                val = _filter_dict_by_path_and_func(v, path[1:], func)
            else:
                val = _filter_dict_by_path_and_func(v, path, func)
            if val:
                new_dict[k] = val
    return new_dict


def _get_matching_fields(my_dict, field_name):
    values = []
    def inner(sub_dict):
        for k, v in sub_dict.items():
            if k == field_name:
                values.append(v)
            elif isinstance(v, dict):
                inner(v)
        return None
    inner(my_dict)

    return values


# Tuples stuff. Maybe a bad approach
def get_all_matching_path_as_tuples(cities_dict, path):
    tuple_list = _dict_to_tuple_list(cities_dict)
    matches = _filter_tuple_list_by_path(tuple_list, path)
    return matches


def _dict_to_tuple_list(cities_dict):
    entries = []
    for k, v in cities_dict.items():
        if isinstance(v, dict):
            vals = _dict_to_tuple_list(v)
            for val in vals:
                val[0].insert(0, k)
                entries.append(val)
        else:
            entries.append( ([k], v) )
    return entries


def _filter_tuple_list_by_path(tuples, path):
    def inner(tuple_path, filter_path):
        if len(filter_path) == 0:
            return True
        elif len(tuple_path) == 0:
            return False
        elif filter_path[-1] != tuple_path[-1]: # Check lengths first to prevent index out of range errors
            return False
        else:
            return inner(tuple_path[0:-1], filter_path[0:-1])
    
    return list(filter(lambda t : inner(t[0], path), tuples))
