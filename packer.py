def pack(rows):
    return _assemble_cities_dict(rows)

def _assemble_cities_dict(rows):
    headings = _get_headings(rows)
    print(headings[0])
    print(headings[1])
    
    return None

def _get_headings(rows):
    heading_rows = [rows[0]]
    for i in range(1, len(rows)):
        if rows[i][0] != '':
            break
        heading_rows.append(rows[i])

    heading_lengths = []
    for row in heading_rows:
        new_row = []
        for cell in row:
            if cell == '' and len(new_row) != 0:
                new_row[-1] += 1
            else:
                new_row.append(1)
        heading_lengths.append(new_row)

    return (heading_rows, heading_lengths)
            