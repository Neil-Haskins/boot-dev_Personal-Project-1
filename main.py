import parser
import packer
        

def main():
    rows = parser.parse_file(open('data/example_2.csv', 'r'))
    cities = packer.pack(rows)

    print(cities)



main()