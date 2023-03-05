#Python program to get a string made of the first 2 and the last 2 chars from a given a string.
str=input('')
if len(str)<2:
    print('empty string')
print(str[0],str[1],str[-2],str[-1],sep=',')