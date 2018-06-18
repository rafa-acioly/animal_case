[![CircleCI](https://circleci.com/gh/rafa-acioly/animal_case/tree/master.svg?style=svg)](https://circleci.com/gh/rafa-acioly/animal_case/tree/master)

# Animal case convert camelCase to snakeCase and vice-versa

## Usage:

### snake case
```py
from animal_case.convert import to_snake_case

converted = to_snake_case('myRandomString')
print(converted) # output: my_random_string
```

### camel case
```py
from animal_case.convert import to_camel_case

converted = to_camel_case('my_random_string')
print(converted) # output: myRandomString
```

### convert dict keys

* to snake case
```py
from animal_case.convert import keys_to_snake_case

my_dict = {
    "firstKey": 1,
    "secondKey": 2,
    "thirdKey": 3
}

converted = keys_to_snake_case(my_dict)
# output
'''
{
    "first_key": 1,
    "second_key": 2,
    "third_key": 3
}
'''
```

* to camel case
```py
from animal_case.convert import keys_to_snake_case

my_dict = {
    "first_key": 1,
    "second_key": 2,
    "third_key": 3
}

converted = keys_to_camel_case(my_dict)
# output
'''
{
    "firstKey": 1,
    "secondKey": 2,
    "thirdKey": 3
}
'''
```



### Converting dict keys recursively
By default `parse_keys` convert keys to `snake_case`
```py
from animal_case.convert import parse_keys

my_dict = {
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

converted = parse_keys(my_dict)
# output
'''
{
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
'''
```


```py
from animal_case.convert import parse_keys

my_dict = {
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

converted = parse_keys(my_dict, type='camel')
# output
'''
{
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
'''
```
