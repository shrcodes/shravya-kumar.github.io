#Python program to remove the nth index character from a nonempty string.
str=input('enter a string')
i=int(input('type in the index of character to be removed: '))
str=str[:i]+str[i+1:]
print(str)

