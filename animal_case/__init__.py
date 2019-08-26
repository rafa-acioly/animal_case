from typing import Dict, List, Union, Iterable
import re

from .types import SNAKE_CASE, CAMEL_CASE

def _unpack(data) -> Iterable:
    if isinstance(data, dict):
        return data.items()
    return data


def to_snake_case(value: str) -> str:
    """
    Convert camel case string to snake case
    :param value: string
    :return: string
    """
    first_underscore = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', value)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', first_underscore).lower()


def keys_to_snake_case(content: Dict) -> Dict:
    """
    Convert all keys for given dict to snake case
    :param content: dict
    :return: dict
    """
    return {to_snake_case(key): value for key, value in _unpack(content)}


def to_camel_case(value: str) -> str:
    """
    Convert the given string to camel case
    :param value: string
    :return: string
    """
    content = value.split('_')
    return content[0] + ''.join(word.title() for word in content[1:] if not word.isspace())


def keys_to_camel_case(content: Dict) -> Dict:
    """
    Convert all keys for given dict to camel case
    :param content: dict
    :return: dict
    """
    return {to_camel_case(key): value for key, value in _unpack(content)}


def parse_keys(data: Union[Dict, List] = None, types=SNAKE_CASE) -> Union[Dict, List]:
    """
    Convert all keys for given dict/list to snake case recursively
    the main type are 'snake' and 'camel'
    :param data: dict | list
    :return: dict | list
    """
    if types not in (SNAKE_CASE, CAMEL_CASE):
        raise ValueError("Invalid parse type, use snake or camel")
    
    if not isinstance(data, (list, dict)):
        raise TypeError("Invalid data type, use list or dict")

    formatter = keys_to_snake_case if types == 'snake' else keys_to_camel_case

    formatted = type(data)()

    is_dict = lambda x: type(x) == dict
    is_list = lambda x: type(x) == list

    for key, value in _unpack(formatter(data)):
        if is_dict(value):
            formatted[key] = parse_keys(value, types)
        elif is_list(value) and len(value) > 0:
            formatted[key] = []
            for val in value:
                if isinstance(val, (list, dict)):
                    val = parse_keys(val, types)
                formatted[key].append(val)
        else:
            formatted[key] = value
    return formatted
