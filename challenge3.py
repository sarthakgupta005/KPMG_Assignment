import json


def getnestedvalue(key, converted_object):
    splitkey = key.split("/")
    return converted_object[splitkey[0]][splitkey[1]][splitkey[2]]


obj1 = "{\"a1\":{\"b1\":{\"c1\":\"d1\"}}}"
key1 = "a1/b1/c1"
obj1_converted = json.loads(obj1)
print("\nGiven Object - " + obj1)
print("Given Keys - " + key1)
print("Value for given key - " + getnestedvalue(key1, obj1_converted))

obj2 = "{\"x1\":{\"y1\":{\"z1\":\"a1\"}}}"
key2 = "x1/y1/z1"
obj2_converted = json.loads(obj2)
print("\nGiven Object - " + obj2)
print("Given Keys - " + key2)
print("Value for given key - " + getnestedvalue(key2, obj2_converted))
