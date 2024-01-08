import parser
import packer
import filters

from dev import nicely_print_list
        

def main():
    rows = parser.parse_file(open('data/example_1.csv', 'r'))
    cities_dict = packer.pack(rows)

    # print(cities_dict)

    # max_temps = filters.get_max_temps(cities_dict)
    # nicely_print_list(max_temps)
    
    # min_temps = filters.get_min_temps(cities_dict)
    # nicely_print_list(min_temps)





main()