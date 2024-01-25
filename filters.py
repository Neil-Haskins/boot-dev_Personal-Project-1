from dev import nicely_print_list


months = [
    'jan',
    'feb',
    'mar',
    'apr',
    'may',
    'jun',
    'jul',
    'aug',
    'sep',
    'oct',
    'nov',
    'dec'
]


def get_max_temps(c_dict):
    names = [x[0] for x in c_dict.items()]
    nums = [max(_get_matching_fields(x[1], 'Record high')) for x in c_dict.items()]
    return list(zip(names, nums))


def get_min_temps(c_dict):
    names = [x[0] for x in c_dict.items()]
    nums = [min(_get_matching_fields(x[1], 'Record low')) for x in c_dict.items()]
    return list(zip(names, nums))


def filter_months(c_dict, start, end):
    m1 = _month_num(start)
    m2 = _month_num(end)
    if m1 > m2:
        m_list = months[0:m2] + months[m1 - 1:12]
    else:
        m_list = months[_month_num(start) - 1: _month_num(end)]
    filtered =  _filter_dict_by_path(c_dict, [m_list])
    return filtered


def filter_max_temp(c_dict, max_temp):
    maxes = get_max_temps(c_dict)
    matches = list(filter(lambda x : x[1] <= max_temp, maxes))
    names = list(map(lambda x: x[0], matches))
    return _filter_dict_by_path(c_dict, [names])


def filter_min_temp(c_dict, min_temp):
    mins = get_min_temps(c_dict)
    matches = list(filter(lambda x : x[1] >= min_temp, mins))
    names = list(map(lambda x: x[0], matches))
    return _filter_dict_by_path(c_dict, [names])

'''
I want to break up the problem of filtering.
1. Apply multiple filters easily
2. Make filters in a DRY fashion
'''
def _filter_dict_by_path(c_dict, path):
    # This checks if all of path appears, but not if it appears without gaps
    # TODO: a list as an element in the path list shall look for any of the contained elements on the same level
    if len(path) == 0:
        return {}
    new_dict = {}

    def run_check(k, v, path_item):
        if len(path) == 1 and k.lower() == path_item.lower():
            new_dict[k] = v
        elif isinstance(v, dict):
            if k.lower() == path_item.lower():
                return _filter_dict_by_path(v, path[1:])
            else:
                return _filter_dict_by_path(v, path)

    for k, v in c_dict.items():
        value = None
        if isinstance(path[0], list):
            for path_item in path[0]:
                result = run_check(k, v, path_item)
                if result:
                    value = result
        else:
            value = run_check(k, v, path[0])
        if value:
            new_dict[k] = value
    return new_dict


def _filter_dict_by_path_and_func(c_dict, path, func):
    # this checks if all of path appears, but not if it appears without gaps
    # the last path item must be the key of the value to be checked
    # func is a function that returns a bool
    if len(path) == 0:
        return {}
    new_dict = {}
    for k, v in c_dict.items():
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


def _get_matching_fields(c_dict, field_name):
    values = []
    def inner(sub_dict):
        for k, v in sub_dict.items():
            if k == field_name:
                values.append(v)
            elif isinstance(v, dict):
                inner(v)
        return None
    inner(c_dict)

    return values


def _month_num(month):
    return months.index(month.lower()) + 1



filters_dict = {
    "Highest temperature": filter_max_temp,
    "Lowest temperature": filter_min_temp,
}