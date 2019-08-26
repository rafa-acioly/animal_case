from __future__ import absolute_import

import pytest

from ..animal_case import to_camel_case, to_snake_case, parse_keys
from ..animal_case.types import CAMEL_CASE, SNAKE_CASE


class TestAnimalCase:

    @pytest.fixture
    def snake_case_dict(self):
        return {
            "first_key": "first value",
            "second_key": "second value",
            "third_key": [
                {"sub_third_key": 1},
                {"sub_third_key2": 2},
                {"sub_third_key3": [
                        {"super_deep": "wow"}
                    ]
                }
            ]
        }

    @pytest.fixture
    def camel_case_dict(self):
        return {
            "firstKey": "first value",
            "secondKey": "second value",
            "thirdKey": [
                {"subThirdKey": 1},
                {"subThirdKey2": 2},
                {"subThirdKey3": [
                        {"superDeep": "wow"}
                    ]
                }
            ]
        }

    def test_convert_string_to_snake_case(self):
        str_camel_case = 'myCamelCaseString'
        assert to_snake_case(str_camel_case) == 'my_camel_case_string'

    def test_convert_string_to_camel_case(self):
        str_snake_case = 'str_in_snake_case'
        assert to_camel_case(str_snake_case) == 'strInSnakeCase'

    def test_convert_dict_keys_to_snake_case(
            self,
            camel_case_dict,
            snake_case_dict
    ):
        converted = parse_keys(camel_case_dict)
        assert converted == snake_case_dict

    def test_convert_dict_keys_to_camel_case(
            self,
            snake_case_dict,
            camel_case_dict
    ):
        converted = parse_keys(snake_case_dict, types=CAMEL_CASE)
        assert converted == camel_case_dict

    def test_invalid_option_parse_keys(self):
        with pytest.raises(ValueError):
            parse_keys({}, 'invalid')

    @pytest.mark.parametrize('key,data_type', [
        ('random', 'camel'),
        (123, 'camel'),
        (None, 'camel'),
        ('random', 'snake'),
        (123, 'snake'),
        (None, 'snake'),
    ])
    def test_invalid_data_type(self, key, data_type):
        with pytest.raises(TypeError):
            parse_keys(key, data_type)

    @pytest.mark.parametrize('values', [
        [1, 2, 3], 1, 1.0, 'string', (1, 2, 3), {1, 2, 3}
    ])
    def test_convert_not_dict_values_to_camel_case(self, values):
        converted = parse_keys({"first_key": values}, types=CAMEL_CASE)
        assert converted == {"firstKey": values}

    @pytest.mark.parametrize('values', [
        [1, 2, 3], 1, 1.0, 'string', (1, 2, 3), {1, 2, 3}
    ])
    def test_convert_not_dict_values_to_snake_case(self, values):
        converted = parse_keys({"firstKey": values})
        assert converted == {"first_key": values}
