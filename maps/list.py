def print_numeric_list(number_list):
    print('------------------ START LIST ------------------')
    for number in number_list:
        print('{} -> {}'.format(number_list.index(number), number))
    print('------------------  END LIST  ------------------')


numberList = [1]

print_numeric_list(numberList)

numberList.append(34)

print_numeric_list(numberList)
