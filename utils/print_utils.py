def print_json(input_map):
    print(input_map)
    print('{')
    line = ''
    tab = 1
    for key, value in input_map.items():
        for i in range(1, tab):
            line = line + '\t'
        line = '{}{}: {},\n'.format(line, key, value)
        line = line[:-1]
    print(line)
    print('}')


def print_test():
    print('a')
    print('\n')
    print('b')
    string = '\n\ths'
    print(string)
    print('b')
