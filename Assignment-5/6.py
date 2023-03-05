#Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
str=input("")
if len(str)>=3:
    if str[-3:]=='ing':
        str+='ly'
    else:
        str+='ing'
    print(str)
else:
    print(str)

    





