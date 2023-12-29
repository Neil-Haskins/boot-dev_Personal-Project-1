import csv
from io import StringIO

def parse_file(file):
    rows = file.read().splitlines()
    parsed_rows = list(map(parse_line, rows))
    return parsed_rows

def parse_line(line):
    csv_file = StringIO(line)
    csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
    row = next(csv_reader)
    return row