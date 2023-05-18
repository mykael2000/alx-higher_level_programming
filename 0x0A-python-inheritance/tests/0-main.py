#!/usr/bin/python3
find = __import__('0-lookup').lookup

class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

print(find(MyClass1))
print(find(MyClass2))
print(find(int))
