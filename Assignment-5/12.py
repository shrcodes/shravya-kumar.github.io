#Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.
def to_uppercase(str):
    count= 0
    for letter in str[:4]: 
        if letter.upper() == letter:
            count+= 1
    if count>= 2:
        return str.upper()
    return str
str=input('')
print(to_uppercase(str))