def nicely_print(val):
    if isinstance(val, list):
        nicely_print_list(val)
    elif isinstance(val, dict):
        nicely_print_dict(val)
    else:
        print(val)

def nicely_print_list(my_list):# just for dev
    print('[')
    for item in my_list:
        if isinstance(item, str):
            item = f'\'{item}\''
        print(f'    {item},')
    print(']')


def nicely_print_dict(my_dict):# just for dev
    def inner(sub_dict, prefix):
        for k, v in sub_dict.items():
            if isinstance(v, dict):
                print(f'{prefix}\'{k}\': {{')
                inner(v, f'{prefix}    ')
                print(f'{prefix}}},')
            else:
                if isinstance(v, str):
                    v = f'\'{v}\''
                print(f'{prefix}\'{k}\': {v},')

    print('{')
    inner(my_dict, '    ')
    print('}')