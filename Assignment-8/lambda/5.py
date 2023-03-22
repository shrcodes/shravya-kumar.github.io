#Write a Python program to check whether a given string is number or not using Lambda
is_number = lambda s: s.replace('.','',1).isdigit()
string1 = "123"
string2 = "3.14"
string3 = "-42"
string4 = "not a number"
print(is_number(string1)) 
print(is_number(string2)) 
print(is_number(string3)) 
print(is_number(string4)) 
