from __future__ import absolute_import
import pytest

from ..animal_case.convert import to_camel_case, to_snake_case, parse_keys


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


    def test_convert_dict_keys_to_snake_case(self, camel_case_dict):
        converted = parse_keys(camel_case_dict)

        assert 'first_key' in converted
        assert 'second_key' in converted
        assert 'third_key' in converted

        assert 'sub_third_key' in converted['third_key'][0]
        assert 'sub_third_key2' in converted['third_key'][1]
        assert 'sub_third_key3' in converted['third_key'][2]

        assert 'super_deep' in converted['third_key'][2]['sub_third_key3'][0]


    def test_convert_dict_keys_to_camel_case(self, snake_case_dict):
        converted = parse_keys(snake_case_dict, types='camel')

        assert 'firstKey' in converted
        assert 'secondKey' in converted
        assert 'thirdKey' in converted

        assert 'subThirdKey' in converted['thirdKey'][0]
        assert 'subThirdKey2' in converted['thirdKey'][1]
        assert 'subThirdKey3' in converted['thirdKey'][2]
        assert 'superDeep' in converted['thirdKey'][2]['subThirdKey3'][0]


    def test_invalid_option_parse_keys(self):
        with pytest.raises(ValueError):
            parse_keys({}, 'invalid')
