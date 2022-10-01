"""Interface module."""

import sys

from .config import STORE_PATH, EXPORT_PATH, IMPORT_PATH
from .utils import (
    get_numbers,
    is_entry_valid,
    convert_to_csv,
)


def close():
    print('Exiting app...!')
    sys.exit()


def read_entries():
    entries = ''

    with open(STORE_PATH, 'r', encoding='utf8') as f:
        entry = []

        for n, value in enumerate(f.readlines(), start=1):
            entry.append(value.strip())

            if not n%4:
                entry_string = (
                    'Last name: {}, '
                    'First Name: {}, '
                    'Phone number: {}, '
                    'Description: {}'
                ).format(*entry)

                entries += f'{entry_string}\n'
                entry = []

    return entries


def input_phone():
    while True:
        phone = input('Enter your phone_number: (11 digits): ')
        clear_phone = get_numbers(phone)
        if len(clear_phone) != 11:
            print('The phone_number must have 11 digits!')
            continue

        return clear_phone.strip()


def input_entry():
    data = [
        input('Enter your last_name: ').strip(),
        input('Enter a first_name: ').strip(),
        input_phone(),
        input('Enter a description: ').strip(),
    ]

    return data


def write_entry(data):
    if is_entry_valid(data):
        with open(STORE_PATH, 'a', encoding='utf8') as f:
            f.write('\n'.join(data))
    else:
        print(f'Broken entry: {data}')


def add_entry():
    write_entry(input_entry())


def export_data():
    file_format = input('Use csv format (Blank - "No")? ')
    with open(EXPORT_PATH, 'w', encoding='utf8') as export_f:
        with open(STORE_PATH, 'r', encoding='utf8') as f:
            data = f.readlines()

            if file_format != '':
                data = convert_to_csv(data)

            export_f.writelines(data)


def import_data():
    file_format = input('Use csv format (Blank - "No")? ')
    with open(IMPORT_PATH, 'r', encoding='utf8') as import_file:
        lines = import_file.readlines()
        if file_format == '':
            lines = convert_to_csv(lines)

        for entry in lines:
            write_entry(entry.split(';'))


def unknown_action():
    return 'Action not recognized.'


def get_actions():
    return {
        0: ('Exit', close),
        1: ('Read entries', read_entries),
        2: ('Add entry', add_entry),
        3: ('Export to file', export_data),
        4: ('Import file', import_data)
    }


ACTIONS = get_actions()

MENU = 'Available actions:\n' + '\n'.join(
    f'{k}. {v[0]}' for k, v in ACTIONS.items())


def start_interface():
    print('Welcome to phonebook!\n')

    while True:
        print(MENU)
        action = input('Choose action: ')

        try:
            action_function = ACTIONS[int(action)][1]
        except (KeyError, ValueError):
            action_function = unknown_action

        result = action_function()

        if result:
            print(result)
