import re

def _unpack(data):
    if isinstance(data, dict):
        return data.items()
    return data


def to_snake_case(value):
    """
    Convert camel case string to snake case
    :param value: string
    :return: string
    """
    first_underscore = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', value)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', first_underscore).lower()


def keys_to_snake_case(content):
    """
    Convert all keys for given dict to snake case
    :param content: dict
    :return: dict
    """
    return {to_snake_case(key): value for key, value in _unpack(content)}


def to_camel_case(value):
    """
    Convert the given string to camel case
    :param value: string
    :return: string
    """
    content = value.split('_')
    return content[0] + ''.join(word.title() for word in content[1:] if not word.isspace())


def keys_to_camel_case(content):
    """
    Convert all keys for given dict to camel case
    :param content: dict
    :return: dict
    """
    return {to_camel_case(key): value for key, value in _unpack(content)}


def parse_keys(data, types='snake'):
    """
    Convert all keys for given dict/list to snake case recursively
    the main type are 'snake' and 'camel'
    :param data: dict
    :return: dict

    """
    if types not in ('snake', 'camel'):
        raise Exception("Invalid parse type, use snake or camel")

    formatted = {}
    for key, value in _unpack(
            keys_to_snake_case(data) if type == 'snake' else keys_to_camel_case(data)
    ):
        if isinstance(value, dict):
            formatted[key] = parse_keys(value, types)
        elif isinstance(value, list) and len(value) > 0:
            formatted[key] = []
            for _, val in enumerate(value):
                formatted[key].append(parse_keys(val, types))
        else:
            formatted[key] = value
    return formatted
