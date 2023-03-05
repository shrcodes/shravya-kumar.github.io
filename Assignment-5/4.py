#Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.

string='restart'
first=string[0]
for i in range(len(string)):
    if string[i]==first:
        a=string[1:].replace(first,'$')
print(first+a)