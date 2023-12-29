def pack(rows):
    return _assemble_cities_dict(rows)

def _assemble_cities_dict(rows):
    headings = _get_headings(rows)
    heading_rows_num = max(len(lst) for lst in headings)
    city_list = rows[heading_rows_num:]

    tuples = []
    for city in city_list:
        tuples.append(list(zip(city, headings)))

    dicts = list(map(_city_dict, tuples))
    main_dict = {}
    for city in dicts:
        title = f"{city['City']}, {city['Country']}, {city['Region']}"
        main_dict[title] = city
    return main_dict

def _city_dict(city):
    dict = {}
    sub_items = []
    for (val, lst) in city:
        if len(lst) == 1:
            dict[lst[0]] = val
        else:
            title = lst[0]
            if len(sub_items) == 0 or sub_items[-1][0] != title:
                sub_items.append( (title, [(val, lst[1:])]) )
            else:
                sub_items[-1][1].append((val, lst[1:]))

    for name, vals in sub_items:
        dict[name] = _city_dict(vals)

    return dict


def _get_headings(rows):
    heading_rows = [rows[0]]
    for i in range(1, len(rows)):
        if rows[i][0] != '':
            break
        heading_rows.append(rows[i])

    heading_columns = list(map(list, zip(*heading_rows)))
    
    for i in range(len(heading_columns)):
        col = heading_columns[i]
        for j in range(len(heading_columns[i]) - 1, -1,  -1):
            if col[j] == '' and j == len(col) - 1:
                del col[-1]
            elif col[j] == '':
                target = i - 1
                while heading_columns[target][j] == '':
                    target -= 1
                col[j] = heading_columns[target][j]

    return heading_columns
            