# Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
str1=input('enter a string: ')
str2=input('enter a string: ')
str_1=str2[:2]+str1[2:]
str_2=str1[:2]+str2[2:]
print(str_1,str_2)

