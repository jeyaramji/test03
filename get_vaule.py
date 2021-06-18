def iterate_val(dict_value):
    for key, value in dict_value.items():
        if type(value) == dict:
            iterate_val(value)
        else:
            print(value)


if __name__ == '__main__':
    iterate_val({"a": {"b": {"c": "d"}}})
    iterate_val({"x": {"y": {"z": "a"}}})
