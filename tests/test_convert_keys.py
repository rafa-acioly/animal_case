import unittest

from convert_keys import convert

class ConvertKeysTest(unittest.TestCase):

    def test_convert_string_to_snake_case(self):
        str_camel_case = 'myCamelCaseString'
        str_with_space = 'string with spaces'

        self.assertEqual(convert.to_snake_case(str_camel_case), 'my_camel_case_string')
        self.assertEqual(convert.to_snake_case(str_with_space), 'string_with_space')


    def test_convert_dict_keys_to_snake_case(self):
        data = {
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

        converted = convert.parse_keys(data)

        self.assertIn('first_key', converted)
        self.assertIn('second_key', converted)
        self.assertIn('third_key', converted)

        self.assertIn('sub_third_key', converted['third_key'])
        self.assertIn('sub_third_key2', converted['third_key'])
        self.assertIn('sub_third_key3', converted['third_key'])

        self.assertIn('super_deep', converted['third_key']['sub_third_key3'])


    def test_convert_string_to_camel_case(self):
        str_snake_case = 'str_in_snake_case'
        str_with_space = 'str with spaces'

        self.assertEqual(convert.to_camel_case(str_snake_case), 'strInSnakeCase')
        self.assertEqual(convert.to_camel_case(str_with_space), 'strWithSpaces')


    def test_convert_dict_keys_to_camel_case(self):
        data = {
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

        converted = convert.parse_keys(data, type='camel')

        self.assertIn('firstKey', converted)
        self.assertIn('secondKey', converted)
        self.assertIn('thirdKey', converted)

        self.assertIn('subThirdKey', converted['thirdKey'])
        self.assertIn('subThirdKey2', converted['thirdKey'])
        self.assertIn('subThirdKey3', converted['thirdKey'])
        self.assertIn('superDeep', converted['thirdKey']['subThirdKey3'])
