#Write a Python program to find if a given string starts with a given character using Lambda

starts_with = lambda string, char: string.startswith(char)
string = "hello world"
char = "h"
print(starts_with(string, char)) 
char = "w"
print(starts_with(string, char)) 
