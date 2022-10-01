"""Utilities."""


def is_number(symbol: str) -> bool:
    try:
        int(symbol)
        return True
    except ValueError:
        return False


def get_numbers(phone: str) -> str:
    result = []

    for symbol in phone:
        if is_number(symbol):
            result.append(symbol)

    return ''.join(result)


def is_entry_valid(data):
    if len(data) == 4 and len(get_numbers(data[2])) == 11:
        return True

    return False


def convert_to_csv(data):
    lines = []

    if not len(data) % 4:
        entry = []

        for n, value in enumerate(data, start=1):
            entry.append(value.strip())

            if not n % 4:
                entry_string = ','.join(entry) + '\n'
                lines.append(entry_string)
                entry = []

        return lines

    raise Exception('Broken data')
