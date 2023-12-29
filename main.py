import parser
import packer
        

def main():
    rows = parser.parse_file(open('data/example_1.csv', 'r'))
    cities_dict = packer.pack(rows)

    print(cities_dict)



main()