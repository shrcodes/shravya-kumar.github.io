#9.Write a Python program to multiply all the items in a dictionary.
dic={1:10,2:10,3:20,4:5,7:80}
prod=1
for i in dic.values():
    prod=prod*i
print(prod)