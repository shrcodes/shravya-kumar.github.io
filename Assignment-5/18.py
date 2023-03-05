#Write a Python program to swap comma and dot in a string.
#Sample string: "32.054,23"
#Expected Output: "32,054.23"

string="32.054,23"
txt=string.maketrans('.,',',.')
print(string.translate(txt))

