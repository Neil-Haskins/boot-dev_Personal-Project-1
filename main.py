import parser
import packer
import filters
        

def main():
    rows = parser.parse_file(open('data/example_1.csv', 'r'))
    cities_dict = packer.pack(rows)

    # print(cities_dict)
    matches = filters.get_all_matching(cities_dict, ['Record high'])
    _nicely_print_list(matches)

    max_temps = filters.get_max_temp(cities_dict)
    _nicely_print_list(max_temps)


def _nicely_print_list(my_list):# just for dev
    print('[')
    for item in my_list:
        print(f'    {item}')
    print(']')



main()