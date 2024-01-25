import parser
import packer
import filters
import gui

from dev import nicely_print_list, nicely_print_dict, nicely_print
        

def main():
    rows = parser.parse_file(open('data/example_1.csv', 'r'))
    cities_dict = packer.pack(rows)

    root = gui.Window(800, 600, cities_dict)




main()