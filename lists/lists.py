def print_list(number_list):
    print('------------------ START LIST ------------------')
    for number in number_list:
        print('{:d} -> {:d}'.format(number_list.index(number), number))
    print('------------------  END LIST  ------------------')


numberList = [1]

print_list(numberList)

numberList.append(34)

print_list(numberList)
