def pack(rows):
    return _assemble_cities_dict(rows)

def _assemble_cities_dict(rows):
    headings = _get_headings(rows)
    body = rows[len(headings[0]):]
    
    print('\nbody:')
    print('[')
    for row in body:
        print(f'    {row}')
    print(']')


    
    return None

def _get_headings(rows):
    heading_rows = [rows[0]]
    for i in range(1, len(rows)):
        if rows[i][0] != '':
            break
        heading_rows.append(rows[i])

    heading_lists = []
    for i in range(len(heading_rows[0])):
        heading_lists.append([])
        current = ''
        for j in range(len(heading_rows)):
            if heading_rows[j][i] != '':
                current = heading_rows[j][i]
            elif heading_rows[j][i] == '' and current == '':
                current = heading_rows[j][i - 1]
            heading_lists[i].append(current)

    return heading_lists
            