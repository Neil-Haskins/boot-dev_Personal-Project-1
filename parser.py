import csv
from io import StringIO

def parse_file(file):
    rows = file.read().splitlines()
    parsed_rows = list(map(_parse_line, rows))
    return parsed_rows

def _parse_line(line):
    csv_file = StringIO(line)
    csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
    row = next(csv_reader)
    return row