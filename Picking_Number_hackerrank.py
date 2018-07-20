matrix_order = int(input(''))
if (2 <= matrix_order and matrix_order <= 100):
    dictionary = {}
    array_input = input().strip().split(' ')
    array_input_integered = list(map(int, array_input))
    order_set = set(array_input_integered)
    value=[]
    for element in order_set:
        count = 0
        for item in array_input_integered:
            if element == item:
                count += 1
        array_input_integered = array_input_integered
        dictionary[element] = count
        value.append(count)

    #print(dictionary)

    for elements1 in order_set:
        for elements2 in order_set:
            if elements2 - elements1 == 1:
                value.append(int(dictionary.get(elements1) +
                                 dictionary.get(elements2)))

    print(max(value))
else:
    pass
