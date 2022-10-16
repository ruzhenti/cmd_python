def view_data(data, title):
    print(f'{title} = {data}')


def get_value():
    return input()


def input_data():
    print('What numbers will we work with? Enter 1 to work with complex numbers, 2 to work with rational numbers')
    data_type = get_value()
    if data_type == '1':
        print('Enter the first number (use the format: "5 + 3j"):')
        left_value = get_value()
        print('Enter the second number (use the format: "5 + 3j"):')
        right_value = get_value()
        print('Change operation:')
        oper = get_value()
    elif data_type == '2':
        print('Enter the first number (use the format: "5/11"):')
        left_value = get_value()
        print('Enter the second number (use the format: "5/11"):')
        right_value = get_value()
        print('Select an operation:')
        oper = get_value()
    return (data_type, left_value, oper, right_value)
    