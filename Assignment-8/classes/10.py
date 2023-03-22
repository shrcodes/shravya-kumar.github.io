#Write a Python program to get the class name of an instance in Python
class MyClass:
    pass
obj = MyClass()
class_name = type(obj).__name__
print("Class name:", class_name)
