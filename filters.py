def get_max_temp(dict):
    cities = []
    for title, city in dict.items():
        highs = []
        # print(city['City'])
        for month, vals in city['Climate'].items():
            highs.append(vals['Record high'])
        # print(highs)
        cities.append((title, max(highs)))
    # print(cities)
    return cities

def get_all_matching(cities_dict, path):
    tuple_list = _dict_to_tuple_list(cities_dict)
    matches = _filter_by_path(tuple_list, path)
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

def _filter_by_path(tuples, path):
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
