import typing

Acode = typing.NewType('Acode', str)

data_type = {
    "int": "\Ai",
    "float": "\Af",
    "chr": "\Ac",
    "str": "\As",
    "dict": "\Ad",
}


def serialize_dict(input_dict: typing.Dict) -> Acode:
    # serialization protocol of dict object
    result: typing.List[typing.AnyStr] = ["\AA", " "]
    for key, value in input_dict.items():
        if type(key).__name__ in data_type:
            result.append(str(data_type[type(key).__name__]) + str(key))
            result.append(str(data_type[type(value).__name__]) + str(value))
            result.append(" ")
    result.append("\A00")
    return Acode("".join(x for x in result))


def desearlize_binary(acode: Acode) -> typing.Dict:
    # deserialization
    code_array = acode.split(' ')
    if code_array[0] != "\AA" or code_array[-1] != "\A00":
        print("Wrong Protocol")
        raise
    code_array.remove("\AA")
    code_array.pop()
    result_dict = {}
    for code in code_array:
        pair = code.split('\\')
        if len(pair) < 3:
            print("Key or Value missing in one dict item")
            raise
        if pair[1][:2] == "As":
            key_type = "string"
            string_key = pair[1][2:]
        elif pair[1][:2] == "Ac":
            key_type = "char"
            char_key = chr(pair[1][2])
        elif pair[1][:2] == "Ai":
            key_type = "int"
            int_key = int(pair[1][2:])
        elif pair[1][:2] == "Af":
            key_type = "float"
            float_key = float(pair[1][2:])
        else:
            print("Wrong Format")
            raise
        if pair[2][:2] == "As":
            value_type = "string"
            string_value = pair[2][2:]
        elif pair[2][:2] == "Ac":
            value_type = "char"
            char_value = chr(pair[2][2])
        elif pair[2][:2] == "Ai":
            value_type = "int"
            int_value = int(pair[2][2:])
        elif pair[2][:2] == "Af":
            value_type = "float"
            float_value = float(pair[2][2:])
        elif pair[2][:2] == "Ad":
            value_type = "dict"
            dict_value = dict(pair[2][2:])
        else:
            print("Wrong Format")
            raise
        if key_type == "char":
            key = char_key
        if key_type == "int":
            key = int_key
        if key_type == "string":
            key = string_key
        if key_type == "float":
            key = float_key
        if value_type == "char":
            value = char_value
        if value_type == "int":
            value = int_value
        if value_type == "string":
            value = string_value
        if value_type == "dict":
            value = dict_value
        if value_type == "float":
            value = float_value
        result_dict[key] = value
    return result_dict


def serialize(input_dict: typing.Dict):
    with open("bin_store.txt", "w") as f:
        data = serialize_dict(input_dict=input_dict)
        f.write(data)


def deserialize() -> typing.Dict:
    with open("bin_store.txt", "r") as f:
        binary_input = f.read()
        result_dict = desearlize_binary(acode=Acode(binary_input))
        return result_dict


# Testing function
if __name__ == "__main__":
    sample_dict = {
        'x': "Aditya",
        'y': {
                'a': 1,
              },
        'z': 3
    }
    # new_dict = {}
    # for i in range(100000):
    #     new_dict[i] = i
    # new_dict[100000] = 10.2
    # serialize(input_dict=sample_dict)
    deserialized_dict = deserialize()
    print(deserialized_dict)
