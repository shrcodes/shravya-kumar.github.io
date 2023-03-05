#Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'
string='''The lyrics is not that poor! 
The lyrics is poor!'''
a=string.find('not')
b=string.find('poor')
if b>a:
    string= string.replace(string[a:(b+4)], 'good')
    print(string)
else:
    print(string)

