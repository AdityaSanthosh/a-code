import typing
import pickle
import pickletools
import datetime
import struct

Acode = typing.NewType('Acode',str)

def to_code(c:chr)->str:
    if c == '{':
        return "\ADs"
    elif c== '}':
        return "\ADe"
    elif c==' ':
        return "\Aa"
    elif c=="\'":
        return "\Ac"
    elif c==':':
        return "\Aeok"
    elif c==",":
        return "\Aeoi"
    else:
        return str(c)

def code_split(string)->typing.List:
    lst:typing.List[typing.AnyStr] = []
    s = 0
    for i in range(len(string)):
        if string[i]=="\\" and string[i+1]=="A" and string[i+2]=="a":
            lst.append(string[s:i])
            s=i+3
    lst.append(string[i:])
    return lst

def valid_code(string:str) -> bool:
    code_array = code_split(string)
    if code_array[0][:3]!="\AA":
        raise "Wrong Protocol"
    

def serialize_dict(input_dict:typing.Dict)->Acode:
    # serialization protocol
    input_string = str(input_dict)
    print(input_string)
    result = "\AA"
    for c in input_string:
        result += to_code(c)
        print(to_code(c))
    result+="\00"
    # if not valid_code(result):
    #     raise "Wrong Input Dictionary Format"
    return result

def desearlize_binary(binary_data:Acode) -> typing.Dict:
    # deserialization protocol

def serialize(input_dict:typing.Dict):
    with open("bin_store.bin","wb") as f:
        data = serialize_dict(input_dict=input_dict)
        f.write(data)
        return
               

def deserialize() -> typing.Dict:
    with open("bin_store.bin","rb") as f:
        binary_input = f.read()
        result_dict = desearlize_binary(binary_data=binary_input)
        return result_dict

if __name__=="__main__":
    sample_dict = {
        'x' : 1,
        'y' : 2,
        'z' : 3
    }
    # with open("bin_store.bin",'wb') as f:
    #     pickle.dump(sample_dict,f)
    # # with open("bin_store.bin","rb") as f:
    # #     data = f.read()
    # #     print(data.decode())
    # data = b'\x01x\x01\x01y\x02\x01z\x03'
    # print(data.decode())
    acode = serialize_dict(sample_dict)
    print(acode)
    print(valid_code(acode))
