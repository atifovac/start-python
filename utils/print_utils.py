def print_json(input_map):
    print(input_map)
    print('{')
    line = ''
    tab = 1
    for key, value in input_map.items():
        for i in range(0, tab):
            line = line + '\t'
        line = '{}{}: {},\n'.format(line, key, value)
    line = line[:-2]
    print(line)
    print('}')
